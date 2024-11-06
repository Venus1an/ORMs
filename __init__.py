from flask import flask


def create_app(config_name):
    app= Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bella&actual.db'
    app.config['SQLACHELMY_TRACK_MODIFICATIONS'] = False 
    app.config['FLASK_RUN_PORT'] = 5001
    return app