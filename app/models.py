from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin


class Users(UserMixin, db.Document):
    #id = db.ObjectIdField()    
    first_name = db.StringField(max_length=80)
    last_name = db.StringField(max_length=80)
    username = db.StringField(max_length=30)
    email = db.EmailField(required=True)    
    password_hash = db.StringField(required=True, max_length=300)
    profile_picture_path=db.StringField(required=True, max_length=300)


    def __repr__(self):
        return self.username


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


#    def get_id(self):
#        return unicode(self._id)


#    @queryset_manager
#    def get_password_hash(doc_cls, queryset):
#        return queryset.


    @login.user_loader
    def load_user(user_id):
        return Users.objects(id=user_id).first()



class Accounts(db.Document):
    name = db.StringField(max_length=200)
    plan_level = db.StringField(max_length=50)
            

class Memberships(db.Document):
    related_user_id = db.StringField(max_length=200)
    related_account_id = db.StringField(max_length=200)
    related_role_id = db.StringField(max_length=200)
    account_email_address = db.StringField(max_length=200)
    account_phone_number= db.StringField(max_length=20)




