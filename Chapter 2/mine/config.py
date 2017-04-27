class DevConfig(object):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://vic:Dd112211@127.0.0.1:3306/vicDB'
