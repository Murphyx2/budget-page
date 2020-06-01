from app import db

class Users(db.Document):    
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.EmailField(required=True)    
    password_hash = db.StringField(required=True, max_length=50)


class Memberships(db.Document):
    related_user_id = db.StringField(max_length=200)
    related_account_id = db.StringField(max_length=200)
    related_role_id = db.StringField(max_length=200)
    account_email_address = db.StringField(max_length=200)
    account_phone_number= db.StringField(max_length=20)


class Accounts(db.Document):
    name = db.StringField(max_length=200)
    plan_level = db.StringField(max_length=50)
            


