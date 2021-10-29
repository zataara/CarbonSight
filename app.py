from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, HomeUsage
from forms import UserForm, LoginForm, HomeUsageForm, Vehicle
from sqlalchemy.exc import IntegrityError
from support_functions import checkUserId
from werkzeug.exceptions import Unauthorized
import requests
from app_secrets import API_KEY


BASE_URL = "https://www.carboninterface.com/api/v1"



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///carbonsight'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

### Main routes
@app.route('/')
def root():
    '''Homepage directory'''
    return render_template('index.html')

### Route for initially registering a user
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





@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')


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
            return redirect('/<username>')
        else:
            form.username.errors = ['Invalid username/password.']
    return render_template('login.html', form=form)

@app.route('/<username>')
def user_home(username):
    # checkUserId(username)

    user = User.query.get_or_404(username)

    return render_template('user_home.html', user=user)

###  Route for adding a monthly Home Electricity Usage amount ###
@app.route('/<username>/addhomeusage', methods=['GET', 'POST'])
def addHomeUsage(username):

    checkUserId(username)

    form=HomeUsageForm()

    if form.validate_on_submit():
        month = form.month.data
        usage = form.usage.data
        user = User.query.get(username)

        ## API request to Carbon Interface for 
        r = requests.post(f'{BASE_URL}/estimates', 
            json={ "type": "electricity",
                    "electricity_unit": "mwh",
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
    
        return render_template('user_home.html', user=user )

    return render_template('addHomeUsage.html', form=form)



###  Route for adding a Vehicle ###
@app.route('/<username>/addvehicle', methods=['GET', 'POST'])
def addVehicle(username):

    checkUserId(username)

    form=Vehicle()

    if form.validate_on_submit():
        year = form.year.data
        make = form.make.data
        model = form.model.data
        user = User.query.get(username)

        ## API request to Carbon Interface for Vehicle Make, returning make_id
        r_makes = requests.post(f'{BASE_URL}/api/vi/vehicle_makes', 
            headers={"Content-Type":"application/json",
                    "Authorization":f"Bearer {API_KEY}"})
        data = r_makes.json()
        make_id = ''
        for object in data:
            if object["data"]["attributes"]["make"] == make:
                make_id = object["data"]["id"]
                break
        
        ## API request to Carbon Interface for Vehicle model, returning model_id
        r_models = requests.post(f'{BASE_URL}/api/vi/vehicle_makes/{make_id}', 
            headers={"Content-Type":"application/json",
                    "Authorization":f"Bearer {API_KEY}"})
        data = r_models.json()
        model_id = ''
        for object in data:
            if object["data"]["attributes"][f"{year}"] == year and object["data"]["attributes"]["name"] == model:
                model_id = object["data"]["id"]
                break
        

        newVehicle = Vehicle(make, model, year, model_id)

        db.session.add(newVehicle)
        db.session.commit()
    
        return render_template('user_home.html', user=user )

    return render_template('addHomeUsage.html', form=form)





