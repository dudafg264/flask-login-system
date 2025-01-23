from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from flask_bootstrap import Bootstrap5
from wtforms.validators import DataRequired, InputRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(check_deliverability=True)])
    password = PasswordField(label='Password', validators=[InputRequired(), Length(min=8, message="Password must be at least 8 characters long.")])
    submit = SubmitField(label='Log in')


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = "app token"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
