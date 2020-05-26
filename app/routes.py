from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, ContactForm
from app import app


nav = [{'name':'Home', 'url':'/home'},
        {'name':'Login','url':'/login'},
        {'name':'About','url':'/about'},
        ]

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', title='Home'
                            , description="Budget page index"
                            , nav = nav)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, nav = nav)


@app.route('/about', methods=('GET', 'POST'))
def about():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect('/index', nav=nav, description='Algo', title='')
    return render_template('about.html', title='About', description= 'This about the page', nav=nav, form=form)