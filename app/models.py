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


#Both income and Expense items share the same structure
class Income_Expense(db.EmbeddedDocument):
    name = db.StringField(max_length=30)
    actual_amount = db.DecimalField()
    planned_amount = db.DecimalField()         

    def set_values(self, name, actual_amount = 0.0, planned_amount=0.0):
        self.name = name
        self.actual_amount = actual_amount
        self.planned_amount = planned_amount


    def set_actual_amount(self, new_actual_amount):
        self.actual_amount = new_actual_amount

    
    def set_planned_amount(self, new_planned_amount):
        self.planned_amount = new_planned_amount


class Budget_Item(db.EmbeddedDocument):
    income = db.ListField(db.EmbeddedDocumentField(Income_Expense))
    expense = db.ListField(db.EmbeddedDocumentField(Income_Expense))


    def add_income(self, income):
        self.income.append(income)


    def add_expense(self, expense):
        self.expense.append(expense)


    def fill_list_income_expenses_from_json(self, elementName, elementObject):
        elementList = []
        for element in elementObject[elementName]:
            income_expense = Income_Expense()
            income_expense.name = element["name"]
            income_expense.actual_amount = element["actual_amount"]
            income_expense.planned_amount = element["planned_amount"]            
            elementList.append(income_expense)
        
        if elementName is 'incomeItems':
            self.income = elementList            

        else:
            self.expense = elementList        
                    


class Budgets(db.Document):    
    user_id = db.StringField(max_length=100)
    title = db.StringField(max_length=100)
    description = db.StringField(max_length=300)
    total_expenses_planned_amount = db.DecimalField() 
    total_expenses_actual_amount = db.DecimalField()  
    total_income_planned_amount = db.DecimalField() 
    total_income_actual_amount = db.DecimalField()    
    date_created= db.DateTimeField()
    budget_items = db.EmbeddedDocumentField(Budget_Item)

    def set_total_expenses_actual_amount(self, total_actual):
        self.total_expenses_actual_amount = total_actual


    def set_total_expenses_planned_amount(self, total_planned):
        self.total_expenses_planned_amount = total_planned


    def set_total_income_actual_amount(self, total_actual):
        self.total_income_actual_amount = total_actual


    def set_total_income_planned_amount(self, total_planned):
        self.total_income_planned_amount = total_planned


    def set_budget_items(self, budget_items):
        self.budget_items = budget_items


    def set_user_id(self, user_id):
        self.user_id = user_id
    

    def set_title(self, title):
        self.title = title
    

    def create_budget(self, user_id, title, date_created, description=""):
        self.user_id = user_id
        self.title = title        
        self.date_created = date_created
        self.description = description
        self.budget_items = Budget_Item()
        self.total_expenses_planned_amount = 0.0
        self.total_expenses_actual_amount = 0.0
        self.total_income_planned_amount = 0.0
        self.total_income_actual_amount = 0.0


class Transactions(db.Document):
    user_id = db.StringField(max_length=100)
    budget_id = db.StringField(max_length=100)
    description = db.StringField(max_length=300)
    type = db.StringField(max_length=20)
    category = db.StringField(max_length=20)
    amount = db.DecimalField()
    date_created= db.DateTimeField()