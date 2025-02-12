####PRE###########
#pylint::disable = all

######LINKS#######
# https://www.w3schools.com/python/python_mysql_getstarted.asp

######IMPORTS#####
import mysql.connector
import json
import requests

class DBInterface():
    """_summary_
    """

    def __init__(self):
        pass

    def connect_database(self, host_name, user_name, password) -> mysql.connector:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "yourusername",
        password = "your_password"
        )
        return mydb

    def get_user(self, id: str) -> dict:
        #mycursor = mydb.cursor()

        #mycursor.execute("SELECT * FROM customers")
        #myresult = mycursor.fetchall() 
        

        user = {
            "user12121": {
                        "id":1,
                        "name": "Egon",
                        "surname": "Nachname",
                        "username": "user12121",
                        "password": "1234",
                        "phone": "+49182718727",
                        "postcode": "91817",
                        "street": "Street 1",
                        "city": "City",
                        "country": "Utopia",
                        "gender": "m/w/d",
                        "role": "admin",
                        "regular": 1
                    }
        }
        
        return user["user12121"]

    def get_all_user(self):
        pass

