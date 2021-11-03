"""SQLAlchemy models for CarbonSight"""


from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
        db.app = app
        db.init_app(app)


class User(db.Model):
    '''Database model for Users'''

    __tablename__ = 'user'

    def __repr__(self):
        
        u = self
        return f"<User {u.username}>"

    username = db.Column(db.String(20),
                            primary_key=True,
                            nullable=False,
                            unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(2), nullable=False)

    @classmethod
    def sum_electric_usage(self):
        out = 0
        # import code; code.interact(local=dict(globals(), **locals()))

        for row in self.homeusage:
            out = row.usage + out
        return 555

    @classmethod
    def register(cls, username, password, email, first_name, last_name, state):
        """Register user with a hashed password and return that user"""
        
        hashed = bcrypt.generate_password_hash(password)
        #turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode('utf8')
        new_user = cls(
            username=username,
            password=hashed_utf8,
            email=email,
            first_name=first_name,
            last_name=last_name,
            state=state
        )
        db.session.add(new_user)
        return new_user

    @classmethod
    def authenticate(cls, username, pwd):
        '''Check username and password against hashed password stored in db'''

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password,pwd):
            return u
        else:
            return False
    
    homeusage = db.relationship('HomeUsage', backref='user', cascade='all,delete')

    vehicle = db.relationship('Vehicle', backref='user', cascade='all,delete')




class HomeUsage(db.Model):
    '''Database Model for Home Usage'''

    __tablename__ = 'homeusage'

    def __init__(self, username, month_name, usage, carbon_g, carbon_lb, carbon_kg, carbon_mt):
        self.username = username
        self.month_name = month_name
        self.usage = usage
        self.carbon_g = carbon_g
        self.carbon_lb = carbon_lb
        self.carbon_kg = carbon_kg
        self.carbon_mt = carbon_mt

    def __repr__(self):
        
        h = self
        return f'<HomeUsage {h.id} username={h.username} month_name={h.month_name} usage={h.usage}>'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    username = db.Column(db.String(20),
                            db.ForeignKey('user.username'),
                            nullable=False,)
    month_name = db.Column(db.String(50),
                            nullable=False)
    usage = db.Column(db.Integer,
                            nullable=False)
    carbon_g = db.Column(db.Integer, nullable = True)
    carbon_lb = db.Column(db.Integer, nullable = True)
    carbon_kg = db.Column(db.Integer, nullable = True)
    carbon_mt = db.Column(db.Integer, nullable = True)


class Vehicle(db.Model):
    '''Database Model for Vehicles'''

    __tablename__ = 'vehicle'

    def __init__(self, username, name, make, model, year, carbon_interface_id):
        self.username = username
        self.name = name
        self.make = make
        self.model = model
        self.year = year
        self.carbon_interface_id = carbon_interface_id
        
    def __repr__(self):
        
        v = self
        return f'<Vehicle Make:${v.make}, Model:${v.model}, Year:{v.year}>'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    username = db.Column(db.String(20),
                            db.ForeignKey('user.username'),
                            nullable=False)
    name = db.Column(db.String(30),
                            nullable=False)
    make = db.Column(db.String(30),
                            nullable=False)
    model = db.Column(db.String(30),
                            nullable=False)
    year = db.Column(db.Integer, nullable=False)
    carbon_interface_id = db.Column(db.String(), nullable=False)

    # vehicleusage = db.relationship('VehicleUsage', backref='vehicle', cascade='all,delete')



# class VehicleUsage(db.Model):
#     '''Database Model for a Vehicles Usage'''

#     __tablename__ = 'vehicleusage'

#     def __init__(self, vehicle_id, month_name, mileage, carbon_g, carbon_lb, carbon_kg, carbon_mt):
#         self.vehicle_id = vehicle_id
#         self.month_name = month_name
#         self.mileage = mileage
#         self.carbon_g = carbon_g
#         self.carbon_lb = carbon_lb
#         self.carbon_kg = carbon_kg
#         self.carbon_mt = carbon_mt
        
#     def __repr__(self):
        
#         v = self
#         return f'<VehicleUsage Month:${v.month_name}, >'

#     id = db.Column(db.Integer,
#                     primary_key=True,
#                     autoincrement=True,)
#     vehicle_id = db.Column(db.String(20),
#                             db.ForeignKey('vehicle.carbon_interface_id'),
#                             nullable=False)
#     month_name = db.Column(db.String(50), nullable=False)
#     mileage = db.Column(db.Integer, nullable=False)
#     carbon_g = db.Column(db.Integer, nullable=True)
#     carbon_lb = db.Column(db.Integer, nullable=True)
#     carbon_kg = db.Column(db.Integer, nullable=True)
#     carbon_mt = db.Column(db.Integer, nullable=True)