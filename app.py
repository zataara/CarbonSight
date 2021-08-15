from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from forms import UserForm, LoginForm
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///synctify'
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

@app.route('/register', methods=['GET', 'POST'])
def register_user():

    form=UserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        new_user = User.register(username, password, email, first_name, last_name)

        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append('Username taken')
            return render_template('register.html', form=form)
        flash(f'Welcome ${new_user.username}! Successfully Created Your Account! Please Login.', 'success')
        return redirect('/login')
    else:
        return render_template('register.html', form=form)

@app.route('/secret')
def secret():
    return render_template('secret.html')



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
            return redirect('/secret')
        else:
            form.username.errors = ['Invalid username/password.']
    return render_template('login.html', form=form)