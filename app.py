from flask import Flask, request, render_template, redirect, flash, session
from flask.helpers import url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, HomeUsage, Vehicle, VehicleUsage, Flights
from forms import UserForm, LoginForm, HomeUsageForm, VehicleForm, VehicleUsageForm, FlightForm
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import Unauthorized
import requests
import os
import re



BASE_URL = "https://www.carboninterface.com/api/v1"



app = Flask(__name__)

############### SETUP FOR HEROKU DEPLOYMENT #################################
# uri = os.getenv("DATABASE_URL")  # or other relevant config var
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)
# API_KEY = os.environ.get('API_KEY')

############### SETUP FOR DEVELOPMENT ENVIRONMENT ###########################
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///carbonsight'
from app_secrets import API_KEY



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()


### Main routes
@app.route('/')
def home():
    '''Homepage directory'''
    
    return render_template('home.html')
    



### Route for initially registering a user ###
@app.route('/register', methods=['GET', 'POST'])
def register_user():

    form=UserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        state = form.state.data
        new_user = User.register(username, password, email, first_name, last_name, state)

        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append('Username taken')
            return render_template('register.html', form=form)
        flash(f'Welcome ${new_user.username}! Successfully Created Your Account! Please Login.', 'success')
        return redirect('/login')
    else:
        return render_template('register.html', form=form)




### Route for logging a user out ###
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')

### Route for logging a user in ###
@app.route('/login', methods=['GET', 'POST'])
def login_user():

    form=LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.authenticate(username, password)
        if user: 
            flash(f'Welcome back {user.username}!', 'primary')
            session['username'] = user.username
            return redirect('home')
        else:
            form.username.errors = ['Invalid username/password.']
    return render_template('login.html', form=form)




### HOME PAGE FOR A USER ###
@app.route('/home')
def user_home():
    if(not session['username']):
        raise Unauthorized();

    username = session['username']
    user = User.query.get_or_404(username)

    return render_template('user_home.html', user=user)





###  Route for adding a monthly Home Electricity Usage amount ###
@app.route('/home/addhomeusage', methods=['GET', 'POST'])
def addHomeUsage():
    if(not session['username']):
        raise Unauthorized();
    username = session['username']
    

    form=HomeUsageForm()

    if form.validate_on_submit():
        month = form.month.data
        usage = form.usage.data
        user = User.query.get(username)

        ## API request to Carbon Interface for 
        r = requests.post(f'{BASE_URL}/estimates', 
            json={ "type": "electricity",
                    "electricity_unit": "kwh",
                    "electricity_value": usage,
                    "country": "us",
                    "state": user.state},

            headers={"Content-Type":"application/json",
                    "Authorization":f"Bearer {API_KEY}"})
        
        data = r.json()
        carbon_g = data["data"]["attributes"]["carbon_g"]
        carbon_lb = data["data"]["attributes"]["carbon_lb"]
        carbon_kg = data["data"]["attributes"]["carbon_kg"]
        carbon_mt = data["data"]["attributes"]["carbon_mt"]

        newHomeUsage = HomeUsage(user.username, month, usage, carbon_g, carbon_lb, carbon_kg, carbon_mt)

        db.session.add(newHomeUsage)
        db.session.commit()
    
        return redirect(url_for('user_home'))

    return render_template('addHomeUsage.html', form=form)





###  Route for adding a Vehicle ###
@app.route('/home/addvehicle', methods=['GET', 'POST'])
def addVehicle():

    if(not session['username']):
        raise Unauthorized();
    username = session['username']

    form=VehicleForm()

    if form.validate_on_submit():
        year = form.year.data
        make = form.make.data
        model = form.model.data
        name = form.name.data
        user = User.query.get(username)

        ## API request to Carbon Interface for Vehicle Make, returning make_id
        r_makes = requests.get(f'{BASE_URL}/vehicle_makes', 
            headers={"Content-Type":"application/json",
                    "Authorization":f"Bearer {API_KEY}"})
        data = r_makes.json()
        make_id = ''
        for layer in data:
            if layer["data"]["attributes"]["name"] == make:
                make_id = layer["data"]["id"]
                break
        
        ## API request to Carbon Interface for Vehicle model, returning model_id
        r_models = requests.get(f'{BASE_URL}/vehicle_makes/{make_id}/vehicle_models', 
            headers={"Content-Type":"application/json",
                    "Authorization":f"Bearer {API_KEY}"})
        data = r_models.json()
        model_id = ''
        for layer in data:
            if layer["data"]["attributes"]["year"] == year and layer["data"]["attributes"]["name"] == model:
                model_id = layer["data"]["id"]
                break

        newVehicle = Vehicle(username, name, model_id)

        db.session.add(newVehicle)
        db.session.commit()
    
        return redirect(url_for('user_home', user=user ))

    return render_template('addVehicle.html', form=form)




### Route for adding a Vehicle's usage
@app.route('/home/addvehicleusage', methods=['GET', 'POST'])
def addVehicleUsage():
    if(not session['username']):
        raise Unauthorized();
    username = session['username']
    
    vehicles = Vehicle.query.filter(Vehicle.username == username)

    form=VehicleUsageForm()
    form.vehicle.choices = [(v.id, v.name) for v in vehicles]

    if form.validate_on_submit():
        vehicle = int(form.vehicle.data)
        month = form.month.data
        distance = form.distance.data
        days = int(form.days.data)
        remote = form.remote.data
        extra_mileage = form.extra_mileage.data

        v1 = Vehicle.query.get(vehicle)

        if(not remote):
            total_mileage = (distance * 2 * days) + extra_mileage
        else:
            total_mileage = extra_mileage


        ## API request to Carbon Interface for Vehicle estimate
        r = requests.post(f'{BASE_URL}/estimates', 
            json={ "type": "vehicle",
                    "distance_unit": "mi",
                    "distance_value": total_mileage,
                    "vehicle_model_id": v1.carbon_interface_id},

            headers={"Content-Type":"application/json",
                    "Authorization":f"Bearer {API_KEY}"})
        
        data = r.json()
        carbon_g = data["data"]["attributes"]["carbon_g"]
        carbon_lb = data["data"]["attributes"]["carbon_lb"]
        carbon_kg = data["data"]["attributes"]["carbon_kg"]
        carbon_mt = data["data"]["attributes"]["carbon_mt"]

        newVehicleUsage = VehicleUsage(vehicle, month, total_mileage, carbon_g, carbon_lb, carbon_kg, carbon_mt)



        db.session.add(newVehicleUsage)
        db.session.commit()
    
        return redirect(url_for('user_home'))

    return render_template('addVehicleUsage.html', form=form)


###  Route for adding a flight###
@app.route('/home/addflight', methods=['GET', 'POST'])
def addFlight():
    if(not session['username']):
        raise Unauthorized();
    username = session['username']
    

    form=FlightForm()

    if form.validate_on_submit():
        passengers = form.passengers.data
        departure = form.departure.data
        destination = form.destination.data
        leg1 = form.leg1.data
        leg2 = form.leg2.data
        user = User.query.get(username)
        legs = [ {"departure_airport": departure, "destination_airport": destination}]            

        if(leg1 and not leg2):
            legs = [{"departure_airport": departure, "destination_airport": leg1},{"departure_airport": leg1, "destination_airport": destination}
        ]

        if(leg1 and leg2):
            legs = [{"departure_airport": departure, "destination_airport": leg1},{"departure_airport": leg1, "destination_airport": leg2},{"departure_airport": leg2, "destination_airport": destination}
        ]
        
        if(not leg1 and leg2):
            legs = [{"departure_airport": departure, "destination_airport": leg1},{"departure_airport": leg1, "destination_airport": destination}
        ]


        ## API request to Carbon Interface for Flight estimate
        r = requests.post(f'{BASE_URL}/estimates', 
            json={ "type": "flight",
                    "passengers": passengers,
                    "legs": legs,
                    "distance_unit": "mi"},

            headers={"Content-Type":"application/json",
                    "Authorization":f"Bearer {API_KEY}"})
        
        data = r.json()
        mileage = data["data"]["attributes"]["distance_value"]
        carbon_g = data["data"]["attributes"]["carbon_g"]
        carbon_lb = data["data"]["attributes"]["carbon_lb"]
        carbon_kg = data["data"]["attributes"]["carbon_kg"]
        carbon_mt = data["data"]["attributes"]["carbon_mt"]

        newFlight = Flights(user.username, departure, destination, mileage, carbon_g, carbon_lb, carbon_kg, carbon_mt)

        db.session.add(newFlight)
        db.session.commit()
    
        return redirect(url_for('user_home'))

    return render_template('addFlight.html', form=form)











### Back End Routes for Javascript Usage
@app.route('/homeUsage/<id>/delete', methods=['POST'])
def deleteHomeUsage(id):
    usage = HomeUsage.query.get(int(id))
    db.session.delete(usage)
    db.session.commit()
    return

@app.route('/vehicleUsage/<id>/delete', methods=['POST'])
def deleteVehicleUsage(id):
    usage = VehicleUsage.query.get(int(id))  
    db.session.delete(usage)
    db.session.commit()
    return

@app.route('/flight/<id>/delete', methods=['POST'])
def deleteFlight(id):
    usage = Flights.query.get(int(id))
    db.session.delete(usage)
    db.session.commit()
    return


    


