class Config(object):
    SECRET_KEY = '736670cb10a600b695a55839ca3a5aa54a7d7356cdef815d2ad6e19a2031182b'
    RECAPTCHA_PUBLIC_KEY = "6LdiCxsUAAAAAKYNF95NmVvMRlwNsgJLfnQn0N6c"
    RECAPTCHA_PRIVATE_KEY = '6LdiCxsUAAAAAJRlIWk8kwp8wzwexKdMUhwvGdpg'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://vic:Dd112211@127.0.0.1:3306/vicDB'



class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://vic:Dd112211@127.0.0.1:3306/vicDB'
