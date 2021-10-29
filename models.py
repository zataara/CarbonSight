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

    def __init__(self, id, make, model, year):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        
    def __repr__(self):
        
        v = self
        return f'<Vehicle>'

    id = db.Column(db.String,
                    primary_key=True,
                    unique=True)
    make = db.Column(db.String(50),
                            nullable=False)
    model = db.Column(db.Integer,
                            nullable=False)
    year = db.Column(db.Integer, nullable = True)
    
    
