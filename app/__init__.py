"""
Return the app after creating our function
"""

from flask import Flask, Blueprint
from app.api.v1.admin.routes import path_1 as meetups
from config import app_config

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(meetups)

    return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)