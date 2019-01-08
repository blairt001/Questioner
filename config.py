"""
This contains our application configurations
"""

class Config:
    """
    This is the default configuration class
    Set Debug to False
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Our development configuration class
    Set Debug to True
    """
    DEBUG = True


class TestingConfig(Config):
    """
    Our testing configuration class
    Set Debug to True
    """
    DEBUG = True

"""
Declaring our application configuration
for development and testing
"""
app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig
}