import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor , CKEditorField 
from flask_wtf import CSRFProtect  # if you want to enable CSRF protect, uncomment this line


app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'
app.config['CKEDITOR_ENABLE_CSRF'] = True  # if you want to enable CSRF protect, uncomment this linE
app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')
app.config['SECRET_KEY'] =  'c3fd3ca1d862453e82b5f62641a51d4d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['CKEDITOR_ENABLE_CODESNIPPET'] = True
app.config['WTF_CSRF_TIME_LIMIT'] = None
app.config['RECAPTCHA_PRIVATE_KEY'] = ''
app.config['RECAPTCHA_PUBLIC_KEY'] = ''


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
ckeditor = CKEditor(app)
csrf = CSRFProtect(app)  # if you want to enable CSRF protect, uncomment this line
from main import routes
