

class Config:
    SECRET_KEY = '4cc37f038e01812d484bbba2d0d9070a'
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:m@localhost/lodge"
    # mysql+mysqldb://root:pass@23.92.23.113/mydb
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class Production(Config):
    DEBUG  = False