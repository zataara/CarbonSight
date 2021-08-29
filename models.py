from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
        db.app = app
        db.init_app(app)


class User(db.Model):
    '''Database model for Users'''

    __tablename__ = 'users'

    def __repr__(self):
        
        u = self
        return f'<User {u.id} username={u.username} name={first_name} {last_name}>'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    username = db.Column(db.String(20),
                            nullable=False,
                            unique=True)
    password = db.Column(db.String,
                            nullable=False)
    first_name = db.Column(db.String(30),
                            nullable=False)
    last_name = db.Column(db.String(30),
                            nullable=False)
    img_url = db.Column(db.String)

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """Register user with a hashed password and return that user"""
        
        hashed = bcrypt.generate_password_hash(password)
        #turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode('utf8')
        new_user = cls(
            username=username,
            password=hashed_utf8,
            email=email,
            first_name=first_name,
            last_name=last_name
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
    

class Artist(db.Model):
    '''Database model for Artists'''

    __tablename__ = 'artists'

    def __repr__(self):
        
        a = self
        return f'<Artists {a.id} >'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(40),
                            nullable=False,
                            unique=True)
    img_url = db.Column(db.String)



artist_user = db.Table('artist_user',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True))

following = db.Table('following',
    db.Column('followee_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id'), primary_key=True))






