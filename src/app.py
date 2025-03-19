####PRE###########
#pylint::disable = all

from flask import(
    jsonify,
    render_template,
    request,
)
import re
import json
import time
import datetime
import MySQLdb.cursors
from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from argon2 import PasswordHasher, exceptions
import random


hasher = PasswordHasher()


app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config['SECRET_KEY'] = 'your_secret_key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'funrestdatabase'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:)vs@Q?95yPFBP5L@localhost:8080/funrestdatabase'

mysql = MySQL(app)



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_list = get_users()
        print(user_list)
        retmsg = { "msg": "Invalid credentials", "code": 401 }  # Standard-Fehlermeldung setzen

        for user in user_list:
            try:
                print(f"\n {user['username']} eingegebene Username {username} \n verify {hasher.verify(user['password'], password)}")
                if user['username'] == username and hasher.verify(user['password'], password):
                    print("gefunden")
                    user = User(username)
                    login_user(user)
                    return redirect(url_for('protected'))
                else:
                    print("fail")
                    retmsg = { "msg": "Invalid Username or Password", "code": 200 }

            except Exception as e:
                print(f"Login-Fehler: {e}")
                retmsg = { "msg": "Invalid credentials", "code": 401 }

        return jsonify(retmsg["msg"]), retmsg["code"] 
    return render_template('login.html')

@app.route('/protected')
@login_required
def protected():
    return f'Hello, {current_user.id}! You are logged in.'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
def homepage():
    return render_template('index.html')
    

@app.route('/register')
def register_page():
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    password = hasher.hash("lebonbon")
    add_user(cursor, "lebronjames", "lebonbon@gmail.com", password, "lebron", "james", "m", "2022-01-01", "91828", "miami", "18th street", "01921818", "1")
    return render_template('register.html')

@app.route('/forget')
def forget_page():
    return render_template('forget.html')

@app.route('/impressum')
def impressum_page():
    return render_template('impressum.html')

@app.route('/agb')
def agb_page():
    return render_template('agb.html')

@app.route('/bewertungen')
def bewertungen_page():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM bewertungen;')

    bewertungen_list = cursor.fetchall()
    return json.dumps(bewertungen_list)

@app.route('/rooms', methods = ['GET'])
def rooms():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM hotelroom;')
    room_list = cursor.fetchall()

    print(room_list)
    return json.dumps(room_list)

@app.route('/ratings', methods = ['GET'])
def ratings():
    ratings = get_ratings()
    return ratings

@app.route('/about')
def about_page():
    return render_template('about.html')
 
@app.route('/leistungen')
def leistungen_page():
    return render_template('leistungen.html')
 
@app.route('/reviews')
def reviews_page():
    return render_template('reviews.html')
 
@app.route('/rooms')
def rooms_page():
    return render_template('rooms.html')
 
def get_ratings():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM rating;')
    rating_list = cursor.fetchall()

    print(rating_list)
    return json.dumps(rating_list)

def get_users():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users;')
    user_list = cursor.fetchall()
    return user_list

def add_user(cursor, username, email, password, firstname, lastname, gender, birthdate, postcode, city, street, phone, regularguest):
    password = hasher.hash(password)
    cursor.execute(f"INSERT INTO `user` (`username`, `email`, `password`, `create_time`, `firstname`, `lastname`, `gender`, `birthdate`, `postcode`, `city`, `street`, `phone`, `regularguest`) VALUES ('{username}', '{email}', '{password}',current_timestamp(), '{firstname}', '{lastname}', '{gender}', '{birthdate}', '{postcode}', '{city}', '{street}', '{phone}', '{regularguest}');")
    cursor.connection.commit()

    return f"added user: {username}"

def remove_user(cursor, username):
    cursor.execute(f"DELETE FROM user WHERE username='{username}';")
    cursor.connection.commit()

def add_room(cursor, roomname, kategorie, preis):
    cursor.execute(f"INSERT INTO `hotelroom` (`roomname`, `kategorie`, `preis`) VALUES ('{roomname}', '{kategorie}', '{preis}');")
    cursor.connection.commit()

def remove_room(cursor, roomid):
    cursor.execute(f"DELETE FROM hotelroom WHERE roomid='{roomid}';")
    cursor.connection.commit()

def add_review(cursor, title, desc, date, userid):
    cursor.execute(f"INSERT INTO `hotelroom` (`title`, `desc`, `date`, `userid`) VALUES ('{title}', '{desc}', '{date}', '{userid}');")
    cursor.connection.commit()


def remove_review(cursor, reviewid):
    cursor.execute(f"DELETE FROM review WHERE reviewid='{reviewid}';")
    cursor.connection.commit()

def select_reviews(cursor):
    cursor.execute(f"SELECT * FROM review;")
    result = cursor.fetchall()

    return json.dumps(result)

def select_review(cursor, id):
    cursor.execute(f"SELECT * FROM review WHERE reviewid = '{id}';")
    result = cursor.fetchall()
    return json.dumps(result)








def get_app():
    return app
