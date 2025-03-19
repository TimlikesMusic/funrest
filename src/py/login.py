####PRE###########
#pylint::disable = all

from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from argon2 import PasswordHasher

app = Flask(__name__, template_folder="test")
app.config['SECRET_KEY'] = 'your_secret_key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'funrestdatabase'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:)vs@Q?95yPFBP5L@localhost:8080/funrestdatabase'

mysql = MySQL(app)




hasher = PasswordHasher()
class User(UserMixin):
    def __init__(self, id):
        self.id = id


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM user;')
        user_list = cursor.fetchall()

        print(user_list)
        print(username)
        print(password)

        for user in user_list:
            try:
                if user['username'] == username and hasher.verify(user['password'], password):
                    user = User(username)
                    login_user(user)
                    return redirect(url_for('protected'))
                return 'Invalid credentials'
            
            except:
                return 'invalid credentials'
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

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    password = hasher.hash("peter")
    add_user(cursor, 140, "lebronjames", "lebonbon@gmail.com", password, "lebron", "james", "m", "2022-01-01", "91828", "miami", "18th street", "01921818", "1")

    return "test"

def add_user(cursor, userid, username, email, password, firstname, lastname, gender, birthdate, postcode, city, street, phone, regularguest):
    cursor.execute(f"INSERT INTO `user` (`userid`, `username`, `email`, `password`, `create_time`, `firstname`, `lastname`, `gender`, `birthdate`, `postcode`, `city`, `street`, `phone`, `regularguest`) VALUES ('{userid}', '{username}', '{email}', '{password}',current_timestamp(), '{firstname}', '{lastname}', '{gender}', '{birthdate}', '{postcode}', '{city}', '{street}', '{phone}', '{regularguest}');")
    cursor.connection.commit()

def add_room():
    pass

def remove_room():
    pass

if __name__ == '__main__':
    app.run(debug=True)