from app import app
from app.forms import LoginForm, ContactForm, createBugdetForm
from app.models import Users, Budgets, Transactions
from app import db
from flask import render_template, flash, redirect, url_for, make_response, flash, request
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from datetime import datetime

import json
from bson import ObjectId

#Module to create testing date
from app import testingDataCreator

nav = [{'name':'Home', 'url':'/home'},  
        {'name':'Transactions','url':'/transactions'},
        {'name':'Budget','url':'/budget'},
        {'name':'About','url':'/about'},                
        ]


@app.route('/')
@app.route('/home')
def index():    
    return render_template('home.html', title='Home', description="Budget page index", nav = nav, user=current_user)


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
        #Insert Navegation items into the nav list. Need of a function to handle this case.
        #nav.insert(1,{'name':'Transactions','url':'/transactions'})        
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in or Register', form=form, nav = nav)


@app.route('/about', methods=['GET','POST'])
def about():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect('/index', nav=nav, description='Algo', title='')
    return render_template('about.html', title='About', description= 'This about the page', nav=nav, form=form, user=current_user)


@app.route('/budget', methods=['GET','POST'])
@login_required
def budget():    
    form = createBugdetForm(request.form)    
    budgets = Budgets.objects(user_id=current_user.get_id()).order_by('-date_created')
    #Validation messages are missed, Must be added in the future        
    if request.method == 'POST' and form.validate():                
        budget = Budgets()
        print("Creating a budget")
        budget.create_budget(current_user.get_id(),form.title.data,  datetime.utcnow(), form.description.data)                
        budget.save()        
        redirect(url_for('budget',make_response='GET'))          
    budgetElement = zip(budgets, range(len(budgets)))
    return render_template('budget.html', title='Budget', description='This about the page creating a budget', nav=nav, form=form, budgets=budgetElement, user=current_user)


@app.route('/budget/<budget_id>', methods=['GET'])
@login_required
def unique_budget(budget_id):        
    budget = None            
    titles = ['Items','Planned Amount', 'Actual Amount', 'Difference']        
    if request.method == 'GET':                
        budget = Budgets.objects(user_id=current_user.get_id(), id=budget_id).first()        
        if budget is None:
            flash(' '.join(('Budget with ID = ',budget_id, 'could not be found')))            
            return redirect(url_for('budget'))    
        #Testing data creator
        #testingDataCreator.create_testing_date(budget)
    return render_template('unique_budget.html', title=budget.title, description=budget.description , nav=nav, budget=budget, titles=titles, user=current_user)


@app.route('/register',methods=['GET','POST'])
def register():
    return redirect(url_for('under_construction'))
    #return render_template('register.html', title='Sign in or Register', description='Want to register?', nav=nav)


@app.route('/transactions/', methods=['GET', 'POST'])
@app.route('/transactions/<budget_id>', methods=['GET','POST'])
@login_required
def transactions(budget_id = None):
    #Find all the budgets for this user    
    budgets = Budgets.objects(user_id=current_user.get_id(), id__ne=(ObjectId(budget_id))).order_by('-date_created')    
    print(budgets)
    if request.method == 'GET':
        if budget_id is not None:            
            current_budget = Budgets.objects(user_id=current_user.get_id(), id=ObjectId(budget_id)).first()            
            incomeTransactions = Transactions.objects(user_id=current_user.get_id(), budget_id=str(budget_id), type="income")
            expensesTransactions = Transactions.objects(user_id=current_user.get_id(), budget_id=str(budget_id), type="expense")                                     
        else:
            current_budget = budgets.first()
            budgets = budgets.filter(id__ne=current_budget.id)
            incomeTransactions = Transactions.objects(user_id=current_user.get_id(), budget_id=str(budgets[0].id), type="income")
            expensesTransactions = Transactions.objects(user_id=current_user.get_id(), budget_id=str(budgets[0].id), type="expense")    
    return render_template('transactions.html', title='Transactions', description='Register your transactions here', nav=nav, user=current_user
    , budgetsList=budgets, expenseTransactions=expensesTransactions, incomeTransactions=incomeTransactions, current_budget = current_budget)

@app.route('/incomeTransaction/<budget_id>', methods=['GET', 'POST'])
@login_required
def incomeTransaction(budget_id = None):
    incomeTransactions = Transactions.objects(user_id=current_user.get_id(), budget_id=str(budget_id), type="income")
    return render_template('incomeTransaction.html', incomeTransactions=incomeTransactions) 

@app.route('/expenseTransaction/<budget_id>', methods=['GET', 'POST'])
@login_required
def expenseTransaction(budget_id = None):
    expensesTransactions = Transactions.objects(user_id=current_user.get_id(), budget_id=str(budget_id), type="expense") 
    return render_template('expenseTransaction.html', expenseTransactions=expensesTransactions) 

@app.route('/under_construction')
def under_construction():
    return render_template('under_construction.html', title='Site Under Construction', description='Site not ready', nav=nav, user=current_user)


@app.route('/update_income_expenses', methods=['POST'])
@login_required
def update_income_expenses():        
    incomeJson = json.loads(request.form["income"])
    expenseJson = json.loads(request.form["expense"])      
    budget = Budgets.objects(user_id=current_user.get_id(), id=request.form["budget_id"]).first()               
    #Check if there are any objects like income or expenses, if there isn't any, They should be created with the data delivered.
    budget.budget_items.fill_list_income_expenses_from_json('incomeItems', incomeJson)
    budget.budget_items.fill_list_income_expenses_from_json('expenseItems', expenseJson)
    budget.save()
    budget.reload()    
    return redirect(url_for('budget',budget_id=budget.id))


@app.errorhandler(404)
def not_found(*args):
    """Page not found."""
    return make_response(render_template("404.html"), 404)

@app.route('/logout')
@login_required
def logout():    
    logout_user()
    #Need to add a function to handle this
    #del nav[1]
    return redirect(url_for('index'))


