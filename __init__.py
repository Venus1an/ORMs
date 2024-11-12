from flask import Flask
from flaskr.modelos.modelos import db

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bellayactualv3.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_RUN_PORT'] = 5001
    db.init_app(app)
    return app