from app import app
from app.forms import LoginForm, ContactForm
from app.models import Users
from app import db
from flask import render_template, flash, redirect, url_for, make_response, flash
from flask_login import current_user, login_user, logout_user, login_required


nav = [{'name':'Home', 'url':'/home'},  
        {'name':'Transactions','url':'/transactions'},
        {'name':'Budget','url':'/budget'},
        {'name':'About','url':'/about'},                
        ]

signin = {'name':'Sign in','url':'/login'}
logout = {'name':'Logout','url':'/logout'}

@app.route('/')
@app.route('/home')
def index():             
    return render_template('home.html', title='Home', description="Budget page index", nav = nav, user=None)


@app.route('/login', methods=['GET','POST'])
def login():        
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.objects(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or password')
            return redirect(url_for('login'))                    
        login_user(user, remember=form.remember_me.data)
        flash('Wellcome {name} {lastname}'.format(name=current_user.first_name, lastname=current_user.last_name))
        
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in or Register', form=form, nav = nav)


@app.route('/about', methods=['GET','POST'])
@login_required
def about():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect('/index', nav=nav, description='Algo', title='')
    return render_template('about.html', title='About', description= 'This about the page', nav=nav, form=form)


@app.route('/budget', methods=['GET','POST'])
def budget():
    return redirect(url_for('under_construction'))
    #return render_template('budget.html', title='Budget', description='This about the page creating a budget', nav=nav)


@app.route('/register',methods=['GET','POST'])
def register():
    return redirect(url_for('under_construction'))
    #return render_template('register.html', title='Sign in or Register', description='Want to register?', nav=nav)


@app.route('/transactions', methods=['GET','POST'])
def transactions():
    return redirect(url_for('under_construction'))


@app.route('/under_construction')
def under_construction():
    return render_template('under_construction.html', title='Site Under Construction', description='Site not ready', nav=nav)


@app.errorhandler(404)
def not_found(*args):
    """Page not found."""
    return make_response(render_template("404.html"), 404)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))