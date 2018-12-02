# configuration file


class BaseConfiguration(object):
    DEBUG = True
    TESTING = False

    def __init__(self, URL):
        self.target = URL


class ProductionConfiguration(BaseConfiguration):
    DEBUG = False
    TESTING = False


class TestConfiguration(BaseConfiguration):
    DEBUG = True
    TESTING = True
