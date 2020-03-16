import datetime
from main import db , login_manager , CKEditorField
from flask_login import UserMixin
from slugify import slugify

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model , UserMixin):
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(20) , nullable = False , unique = True)
    password = db.Column(db.String(60) , nullable = False)

    def __repr__(self):
        return f"User('{self.username}' , '{self.password}')"

class Post(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String , nullable = False , unique = True)
    slug = db.Column(db.String , nullable = True , unique = True)
    content = db.Column(db.Text , nullable = False )
    created_date = db.Column(db.String)


    def __init__(self , title , content):
        self.title = title
        self.content = content
        now = datetime.datetime.now()
        self.created_date = now.strftime("%d %m %Y")

    def slug_(self , title):
        self.slug = slugify(title , separator = '+')


    def __repr__(self):
        return f"Post('{self.title}'  , '{self.created_date}')"





