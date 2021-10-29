from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField
from wtforms.validators import InputRequired, Optional, Length, NumberRange, URL, EqualTo



class UserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired(), Length(max=50)])
    first_name = StringField('First Name', validators=[InputRequired(), Length(max=30)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(max=30)])
    state = SelectField('State', choices=[("al", "Alabama"), ("ak", "Alaska"), ("az", "Arizona"), ("ar", "Arkansas"), ("ca", "California"), ("co", "Colorado"), ("ct", "Connecticut"), ("cd", "Washington D.C."), ("de", "Delaware"), ("fl", "Florida"), ("ga", "Georgia"), ("hi", "Hawaii"), ("id", "Idaho"), ("il", "Illinois"), ("in", "Indiana"), ("ia", "Iowa"), ("ks", "Kansas"), ("ky", "Kentucky"), ("la", "Louisiana"), ("me", "Maine"), ("md", "Maryland"), ("ma", "Massachusetts"), ("mi", "Michigan"), ("mn", "Minnesota"), ("ms", "Missouri"), ("MO", "Montana"), ("mt", "Montana"), ("ne", "Nebraska"), ("nv", "Nevada"), ("nh", "New Hampshire"), ("nj", "New Jersey"), ("nm", "New Mexico"), ("ny", "New York"), ("nc", "North Carolina"), ("nd", "North Dakota"), ("oh", "Ohio"), ("ok", "Oklahoma"), ("or", "Oregon"), ("pa", "Pennsylvania"), ("ri", "Rhode Island"), ("sc", "South Carolina"), ("sd", "South Dakota"), ("tn", "Tennessee"), ("tx", "Texas"), ("ut", "Utah"), ("vt", "Vermont"), ("va", "Virginia"), ("wa", "Washington"), ("wv", "West Virginia"), ("wi", "Wisconson"), ("wy", "Wyoming")])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[InputRequired()])

class HomeUsageForm(FlaskForm):
    month = StringField('Month', validators=[InputRequired(), Length(max=30)])
    usage = IntegerField('Usage', validators=[InputRequired(), NumberRange(min=1, max=None)])

class Vehicle(FlaskForm):
    year = IntegerField('Year', validators=[InputRequired(), NumberRange(min=1900, max=2025)])
    make = SelectField('Make', choices=[("Acura"), ("Alfa Romeo"), ("Aston Martin"), ("Audi"), ("Bentley"), ("BMW"), ("Bugatti"), ("Buick"), ("Cadillac"), ("Chevrolet"), ("Chrysler"), ("Dodge"), ("Ferrari"), ("Fiat"), ("Ford"), ("General Motors"), ("GMC"),  ("Honda"), ("Hyundai"), ("Infiniti"), ("Isuzu"),("Jaguar"), ("Jeep"), ("Kia"), ("Koenigsegg"),  ("Lamborghini"), ("Land Rover"), ("Lexus"), ("Lincoln"), ("Lotus"), ("Maserati"), ("Mazda"), ("Mercedes Benz"), ("Mercury"),  ("Mini"), ("Mitsubishi"), ("Nissan"), ("Plymouth"), ("Pontiac"),   ("Porsche"), ("Ram"), ("Rolls Royce"), ("Saab"), ("Saturn"), ("Shelby"), ("Smart"), ("Subaru"), ("Suzuki"), ("Toyota"), ("Tesla"), ("Volkswagon"), ("Volvo")])
    model = StringField('Model', validators=[InputRequired(), Length(max=20)])





