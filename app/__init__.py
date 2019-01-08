"""
Return the app after creating our function
"""

from flask import Flask, Blueprint

from config import app_config


def create_app(app_environment):
    app = Flask(__name__)
    app.config.from_object(app_config[app_environment])

    return app