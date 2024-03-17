from flask_wtf import FlaskForm 
from wtforms.fields import StringField, EmailField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Length, DataRequired



class LoginForm(FlaskForm):
    email = EmailField("Email")
    senha = PasswordField("Senha", validators=[
        Length(8, 16, "O campo deve conter entre 8 a 16 caracteres.")
    ])
    remember = BooleanField("Permanecer Conectado")
    submit = SubmitField("Entrar")


