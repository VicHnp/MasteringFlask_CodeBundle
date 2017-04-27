class Config(object):
    SECRET_KEY = '736670cb10a600b695a55839ca3a5aa54a7d7356cdef815d2ad6e19a2031182b'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://vic:Dd112211@127.0.0.1:3306/vicDB'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://vic:Dd112211@127.0.0.1:3306/vicDB'