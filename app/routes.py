from app import app
from app.forms import LoginForm, ContactForm, createBugdetForm
from app.models import Users, Budgets,Budget_Item, Income_Expense
from app import db
from flask import render_template, flash, redirect, url_for, make_response, flash, request
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from datetime import datetime


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
def about():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect('/index', nav=nav, description='Algo', title='')
    return render_template('about.html', title='About', description= 'This about the page', nav=nav, form=form)


@app.route('/budget', methods=['GET','POST'])
@login_required
def budget():    
    form = createBugdetForm()
    budgets = Budgets.objects(user_id=current_user.get_id()).order_by('-date_created')  
    if request.method == 'POST':        
        budget = Budgets()
        budget.user_id = current_user.get_id()
        budget.title = form.title.data
        budget.description = form.description.data  
        budget.date_created = datetime.utcnow()      
        budget.save()                             
        redirect(url_for('budget',make_response='GET'))                                  
    return render_template('budget.html', title='Budget', description='This about the page creating a budget', nav=nav, form=form, budgets=budgets)

@app.route('/budget/<budget_id>', methods=['GET','POST'])
@login_required
def check_budget(budget_id):
    flash('Budget requested does not exists {0}'.format(budget_id))
    return redirect(url_for('under_construction'))


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


