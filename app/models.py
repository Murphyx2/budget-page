from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin


class Users(UserMixin, db.Document):    
    first_name = db.StringField(max_length=80)
    last_name = db.StringField(max_length=80)    
    email = db.EmailField(required=True)    
    password_hash = db.StringField(required=True, max_length=300)
    profile_picture_path=db.StringField(required=True, max_length=300)


    def __repr__(self):
        return self.email


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    @login.user_loader
    def load_user(user_id):
        return Users.objects(id=user_id).first()


class Income_Expense(db.EmbeddedDocument):
    name = db.StringField(max_length=30)
    actual_amount = db.DecimalField()
    planned_amount = db.DecimalField() 


    def set_values(self, name, actual_amount, planned_amount):
        self.name = name
        self.actual_amount = actual_amount
        self.planned_amount = planned_amount



class Budget_Item(db.EmbeddedDocument):
    income = db.ListField(db.EmbeddedDocumentField(Income_Expense))
    expense = db.ListField(db.EmbeddedDocumentField(Income_Expense))


    def set_income(self, income):
        self.income.append(income)


    def set_expense(self, expense):
        self.expense.append(expense)


class Budgets(db.Document):    
    user_id = db.StringField(max_length=100)
    title = db.StringField(max_length=100)
    description = db.StringField(max_length=300)
    date_created= db.DateTimeField()
    budget_items = db.EmbeddedDocumentField(Budget_Item)


    def set_user_id(self, user_id):
        self.user_id = user_id
    

    def set_title(self, title):
        self.title = title
    

    def set_budget_items(self, budget_items):
        self.budget_items = budget_items

    def create_budget(self, user_id, title, date_created, description=""):
        self.user_id = user_id
        self.title = title        
        self.date_created = date_created
        self.description = description





