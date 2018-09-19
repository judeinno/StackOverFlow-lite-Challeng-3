import os

class Config(object):
    """The class give my app a default configuration to:
        Be inherited from by other configuration modes
        Provide a secret key
    """
    DEBUG = False
    SECRET = os.getenv('SECRET')
    DATABASE_URL = 'postgres://zpjvmcqxwjigzl:122757e0bba2514559a5bfb9ea75b478d7ceaba2bd50d8198947ee5d767768d5@ec2-54-235-178-189.compute-1.amazonaws.com:5432/darq5mdc6ve3rv'




class ProductionConfig(Config):
    """The class provides configurations at production hence:
        Debug is false
        And testing is false
    """
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """The class provides configurations during development hence:
            Debug is True to allow us get more insite error problems
        """
    DEBUG = True


class TestingConfig(Config):
    """The class provides configurations during testing hence:
            Debug is true for more insite into error problems
            And testing is true to allow testing of the app
        """
    DEBUG = True
    TESTING = True
    DATABASE_URL = 'postgresql://postgres:ROCKcity1234@localhost:5432/stackoverflowtestdb'

class TestingAnswersConfig(Config):
    """The class provides configurations during testing hence:
            Debug is true for more insite into error problems
            And testing is true to allow testing of the app
        """
    DEBUG = True
    TESTING = True
    DATABASE_URL = 'postgresql://postgres:ROCKcity1234@localhost:5432/stackoverflowtestanswers'
