from app import db


class Users(db.Document):
    name = db.StringFiled()
    

