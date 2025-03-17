from flask import Flask 

from . import db
import app

def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()

    db.init_app(app)
    app.register_blueprint(main)

    return app