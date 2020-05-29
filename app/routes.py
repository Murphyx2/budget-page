from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, ContactForm
from app import app


nav = [{'name':'Home', 'url':'/home'},  
        {'name':'Budget','url':'/budget'},
        {'name':'About','url':'/about'},        
        {'name':'Sign in','url':'/login'},
        ]

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', title='Home'
                            , description="Budget page index"
                            , nav = nav)


@app.route('/login', methods=('GET','POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/home')
    return render_template('login.html', title='Sign in or Register', form=form, nav = nav)


@app.route('/about', methods=('GET', 'POST'))
def about():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect('/index', nav=nav, description='Algo', title='')
    return render_template('about.html', title='About', description= 'This about the page', nav=nav, form=form)


@app.route('/budget', methods=('GET','POST'))
def budget():
    return redirect('/under_construction')
    #return render_template('budget.html', title='Budget', description='This about the page creating a budget', nav=nav)


@app.route('/register',methods=('GET','POST'))
def register():
    return redirect('/under_construction')
    #return render_template('register.html', title='Sign in or Register', description='Want to register?', nav=nav)

@app.route('/under_construction')
def under_construction():
    return render_template('under_construction.html', title='Site Under Construction', description='Site not ready', nav=nav)