from flask_script import Manager
from app import create_app
import pytest
from dotenv import load_dotenv

load_dotenv()

app = create_app("config.BaseConfig")
runner = Manager(app)

@runner.command
def test():
    pytest.main(['-v', '--cov-report', 'term-missing', '--cov=app'])

if __name__ == "__main__":
    runner.run()