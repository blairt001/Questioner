import os
from flask_script import Manager
from app import create_app
import pytest
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV")
app = create_app(APP_ENV)

def test():
    pytest.main(['-v', '--cov-report', 'term-missing', '--cov=app'])

if __name__ == "__main__":
    app.run(debug=True)