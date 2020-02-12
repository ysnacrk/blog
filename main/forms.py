from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired 
from flask_ckeditor import CKEditorField



class Login(FlaskForm):
    username = StringField('Username' , validators=[DataRequired()])
    password = PasswordField('Password' , validators=[DataRequired()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    title = StringField('Title')
    content = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField()
