import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor , CKEditorField 
from flask_wtf import CSRFProtect  
from logging.handlers import RotatingFileHandler
from flask_paranoid import Paranoid
from main.config import Config


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#app config

conf = Config()

print(conf.RECAPTCHA_PRIVATE_KEY)
print(conf.RECAPTCHA_PUBLIC_KEY)

app.config.from_object(conf)
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'
app.config['CKEDITOR_ENABLE_CSRF'] = True  
app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')
app.config['CKEDITOR_ENABLE_CODESNIPPET'] = True
app.config['WTF_CSRF_TIME_LIMIT'] = None

# app.config['SESSION_COOKIE_SECURE'] = True  #only production env. 


#database initialize
db = SQLAlchemy(app)

#bcrypt initialize
bcrypt = Bcrypt(app)

#login initialize
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.session_protection = "strong"

#ckeditor initialize
ckeditor = CKEditor(app)

csrf = CSRFProtect(app)  
csrf.init_app(app)

#logger initialize
handler = RotatingFileHandler('app.log', maxBytes = 100000, backupCount = 3)
logger = logging.getLogger('tdm')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

#secure cookie
paranoid = Paranoid(app)
paranoid.redirect_view = '/'

from main import routes

