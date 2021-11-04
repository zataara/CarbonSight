from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, Length, NumberRange, URL, EqualTo
from library import airports, cars, states



class UserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired(), Length(max=50)])
    first_name = StringField('First Name', validators=[InputRequired(), Length(max=30)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(max=30)])
    state = SelectField('State', choices=states)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[InputRequired()])

class HomeUsageForm(FlaskForm):
    month = StringField('Month', validators=[InputRequired(), Length(max=30)])
    usage = IntegerField('Usage', validators=[InputRequired(), NumberRange(min=1, max=None)])

class VehicleForm(FlaskForm):
    year = IntegerField('Year', validators=[InputRequired(), NumberRange(min=1900, max=2025)])
    make = SelectField('Make', choices=cars)
    model = StringField('Model', validators=[InputRequired(), Length(max=20)])
    name = StringField('Name Your Vehicle', validators=[InputRequired(), Length(max=20)])

class VehicleUsageForm(FlaskForm):
    vehicle = SelectField('Vehicle', choices=[])
    month = StringField('Month', validators=[InputRequired(), Length(max=30)])
    distance = IntegerField('Distance to work')
    days = SelectField('How many days a week do you work?', choices=[(1),(2),(3),(4),(5),(6),(7)])
    remote = BooleanField('I Work Remotely')
    extra_mileage = IntegerField('Extra Monthly Mileage')


class FlightForm(FlaskForm):
    passengers = IntegerField('Passengers',validators=[InputRequired(), NumberRange(min=1, max=4)])
    departure = SelectField('Departure City', choices=airports)
    leg1 = SelectField('Stop 1 (Optional)', choices=airports)
    leg2 = SelectField('Stop 2 (Optional)', choices=airports)
    destination = SelectField('Departure City', choices=airports)

    
    
    
    
    

