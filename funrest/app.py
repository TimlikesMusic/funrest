from flask import(
    jsonify,
    render_template,
    request,
)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class user(db.Model):
    userid: Mapped[int] = mapped_column(primary_key=True)



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root@localhost:4508/funrestdatabase'
db.init_app(app)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route("/test")
def test():
    connection = db()

@app.route('/login')
def login_page():
    return render_template('login.html')

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