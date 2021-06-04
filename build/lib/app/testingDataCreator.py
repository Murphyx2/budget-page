#import sys
# insert at 1, 0 is the script path (or '' in REPL)
#sys.path.insert(1, 'D:/Programing/Developments/Python/Flask_Developments/BudgetPage')

from app.models import Users, Budgets, Budget_Item, Income_Expense
from app import db

def create_testing_date(budget):    
    budget_item = Budget_Item()
    income1 = Income()
    income1.set_values("Paycheck", 35000.0,70000.0)

    income2 = Income()
    income2.set_values("Loans", 5000.0,10000.0)

    income3 = Income()
    income3.set_values("Stocks", 200.0, 2000.0)

    budget_item.add_income(income1)
    budget_item.add_income(income2)
    budget_item.add_income(income3)

    expense1 = Expense()
    expense1.set_values("Food",539.75, 3000.0)

    expense2 = Expense()
    expense2.set_values("Supermarket",2459.15, 8000.0)

    expense3 = Expense()
    expense3.set_values("Transportation",275.00, 4000.0)

    expense4 = Expense()
    expense4.set_values("Rent",0.0, 12500.0)

    expense5 = Expense()
    expense5.set_values("Electrical Bill",4000.53, 4000.53)

    budget_item.add_expense(expense1)    
    budget_item.add_expense(expense2)
    budget_item.add_expense(expense3)
    budget_item.add_expense(expense4)
    budget_item.add_expense(expense5)
    
    budget.set_total_expenses_planned_amount(31500.53)
    budget.set_total_expenses_actual_amount(7274.43)

    budget.set_total_income_planned_amount(82000.0)
    budget.set_total_income_actual_amount(40200.0)
    budget.set_budget_items(budget_item)
    budget.save()
