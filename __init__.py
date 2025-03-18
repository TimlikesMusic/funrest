from flask import Flask 
import src.app as app

def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()
    app.register_blueprint()

    return app