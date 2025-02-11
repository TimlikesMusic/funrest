# hello.py

from interface import DBInterface
import json

from flask import Flask
from flask import request


app = Flask(__name__)
interface = DBInterface()
    

@app.route('/')
def empty():
    return "???"

@app.route('/user_name')
def get_user():
    # Get the value of the 'name' parameter from the URL
    user_name = request.args.get('u')
    user_name = interface.get_user(user_name)
     
    # Greet Hello to name provided in the URL Parameter
    return json.dumps(user_name)
   
app.run()