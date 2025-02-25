from flask import Flask, render_template, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import bcrypt
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '8966'  # Make sure this is your correct password
app.config['MYSQL_DB'] = 'mydatabase'
app.secret_key = '8966rabin'

mysql = MySQL(app)

# Registration form class
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

# Login form class
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

# Search form class
class SearchForm(FlaskForm):
    query = StringField("Search", validators=[DataRequired()])
    submit = SubmitField("Search")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Store data in the database
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO user(name, email, password) VALUES (%s, %s, %s)", (name, email, hashed_password))
        mysql.connection.commit()
        cursor.close()
        flash("Registration successful", "success")
        return redirect(url_for('login'))  # Redirect to login page after successful registration

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Check if user exists
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user WHERE email = %s", [email])
        user = cursor.fetchone()
        cursor.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):  # user[3] is password in database
            flash("Login successful", "success")
            return redirect(url_for('dashboard'))  # Redirect to the dashboard if login is successful
        else:
            flash("Invalid email or password", "danger")
    
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
     return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
