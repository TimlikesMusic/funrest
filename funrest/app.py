from flask import(
    jsonify,
    render_template,
    request,
)
from flask import Flask
from flask_mysqldb import MySQL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re





app = Flask(__name__, template_folder="templates")
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
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user')
        user_list = cursor.fetchall()

        print(user_list)
        print(username)
        print(password)

        for user in user_list:
            if user['username'] == username and user['password'] == password:
                user = User(username)
                login_user(user)
                return redirect(url_for('protected'))
            return 'Invalid credentials'
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

@app.route("/test")
def test():
    pass
    #connection = db()
    

@app.route('/register')
def register_page():
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

"""
Test für JSON-Format
"""
incomes = [
    { 'description': 'salary', 'amount': 5000 }
]

@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204



app.run(debug=True)