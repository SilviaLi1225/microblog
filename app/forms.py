from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    permission_list1 = BooleanField('send email', default=False)
    permission_list2 = BooleanField('access your photo', default=False)
    permission_list3 = BooleanField('access your contact', default=False)
    submit = SubmitField('Sign In')


class AskPermission(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Sign In')
