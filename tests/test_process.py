from flask import Flask, config
from flask.wrappers import Response
from flask import redirect, url_for
import sys
from pytest import fixture

from werkzeug.test import Client
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'D:/Programing/Developments/Python/Flask_Developments/BudgetPage')

from app import app
from app import routes
from app import models
from app.forms import LoginForm 


@fixture
def my_budget():    
    return models.Budgets.objects(user_id='5ed5ea4c71bf3be920c7d753', id='6056748b9f0ea7d3f1ccafef').first()


#Adding amounts to budget items
#income
def test_add_actual_amount(my_budget):        
    assert str(my_budget.id) == '6056748b9f0ea7d3f1ccafef'
    

#expense


#test_add_actual_amount()