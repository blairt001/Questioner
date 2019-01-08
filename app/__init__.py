"""Return the app after creating the app instance """

from flask import Flask

def create_app():
    """"""
    app = Flask(__name__)

    return app