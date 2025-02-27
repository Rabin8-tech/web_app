import os
from flask import Flask, render_template, redirect, url_for, flash, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
import bcrypt
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '8966'  # Use your MySQL password
app.config['MYSQL_DB'] = 'mydatabase'
app.secret_key = '8966rabin'

mysql = MySQL(app)

# Form classes
class SearchForm(FlaskForm):
    query = StringField("Search", validators=[DataRequired()])
    media_type = SelectField("Media Type", choices=[('images', 'Images'), ('audio', 'Audio'), ('video', 'Video')], default='images')
    license_type = SelectField("License Type", choices=[('cc0', 'CC0'), ('publicdomain', 'Public Domain')], default='cc0')
    submit = SubmitField("Search")

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

# Open the dashboard directly
@app.route('/')
def index():
    return redirect(url_for('dashboard'))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        cursor = mysql.connection.cursor()
        try:
            cursor.execute("SELECT * FROM user WHERE email = %s", [email])
            user = cursor.fetchone()
        except Exception as e:
            flash(f"Database error: {e}", "danger")
            cursor.close()
            return redirect(url_for('login'))
        cursor.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            session['user_id'] = user[0]
            flash("Login successful", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password", "danger")
    return render_template('login.html', form=form)

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor = mysql.connection.cursor()
        try:
            cursor.execute("INSERT INTO user (name, email, password) VALUES (%s, %s, %s)", (name, email, hashed_password))
            mysql.connection.commit()
        except Exception as e:
            flash(f"Database error: {e}", "danger")
            cursor.close()
            return redirect(url_for('register'))
        cursor.close()

        flash("Registration successful, please log in.", "success")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Dashboard route – accessible to everyone.
# If a search is submitted by an unauthenticated user, flash a prompt.
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = SearchForm()
    media = []
    selected_media_type = None
    searched = False

    if form.validate_on_submit():
        searched = True
        if session.get('user_id'):
            query = form.query.data
            selected_media_type = form.media_type.data
            license_type = form.license_type.data

            # Request URL from Openverse API
            url = f"https://api.openverse.org/v1/{selected_media_type}/?format=json&q={query}&license={license_type}"
            response = requests.get(url)
            try:
                data = response.json()
                if 'results' in data:
                    media = data['results']
                else:
                    flash("No results found.", "warning")
            except Exception as e:
                flash(f"Error fetching search results: {e}", "danger")
        else:
            flash("Please login if you have an account, otherwise please register.", "warning")

    return render_template('dashboard.html', form=form, media=media, selected_media_type=selected_media_type, searched=searched)

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
