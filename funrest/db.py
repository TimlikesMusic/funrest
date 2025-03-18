from flask import Flask, render_template, request
from flask import current_app, g

import mysql.connector
from flask import current_app

def get_db():
    if 'db' not in g or not g.db.is_connected():
        g.db = mysql.connector.connect(
            host=current_app.config['127.0.0.1'],
            user=current_app.config['root'],
            password=current_app.config[')vs@Q?95yPFBP5L'],
            database=current_app.config['funrestdatabase'],
            ssl_verify_identity=True,
            ssl_ca='SSL/certs/ca-cert.pem'
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None and db.is_connected():
        db.close()

get_db()
close_db()