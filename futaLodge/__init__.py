from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from futaLodge.config import Config

db = SQLAlchemy()
# restapi = Api()
# adminn = restapi.namespace('api/admin', description = "This is the admin rest api")
ma = Marshmallow()

def create_app( config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # restapi.init_app(app)
    ma.init_app(app)
    db.init_app(app)
    
    with app.app_context():
    
        from futaLodge.location.routes import api
        from futaLodge.lodge.routes import lodge
        
        app.register_blueprint(api)
        app.register_blueprint(lodge)
        
        return app

