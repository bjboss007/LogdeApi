import datetime as dt
from marshmallow import Schema, fields, pprint
from flask import Blueprint, jsonify, request
from flask import Flask
from flask_marshmallow import Marshmallow
from marshmallow import fields as fl
from marshmallow import INCLUDE
from flask_sqlalchemy import SQLAlchemy
#         self.created_at = dt.datetime.now()
class Config():  
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:m@localhost/lodge"


    SQLALCHEMY_TRACK_MODIFICATIONS = False



app = Flask(__name__)
ma = Marshmallow(app)
db = SQLAlchemy(app)
app.config.from_object(Config)


api = Blueprint('api', __name__)
app.register_blueprint(api)
class LodgeSchema(ma.Schema):
    class Meta:
        fields = ('id','latitude','longitude','name','location_id','_links')
        unknown = INCLUDE
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("m", id="<id>")
        }
    )
    latitude = fl.Float()



    longitude = fl.Float()
class Lodge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable = False )
    longitude = db.Column(db.Float, nullable = False )
    name = db.Column(db.String(100), nullable =False )
    
    
    
class LodgeService():   
    @staticmethod
    def get_by_id(int: id):
        lodge = Lodge.query.get_or_404(id)
        return lodge
#     name = fields.Str()
#     email = fields.Email()
#     created_at = fields.DateTime()
    


lodge_service = LodgeService()
lodge_schema = LodgeSchema()

# user = User(name="Monty", email="monty@python.org")
# schema = UserSchema()
# result = schema.dump(user)
# print(result)


@api.route("/",methods = ["GET"])
def df():
    return {"message":"I got here"}


@app.route("/<int:id>")
def m(id):
    print("I got here first")
    lodge = Lodge.query.get(id)
    print("I got here here too", lodge)
    result = lodge_schema.dump(lodge)

    return {'lodge':result}, 200



if __name__ == '__main__':



    # SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:m@localhost/lodge"
    # # mysql+mysqldb://root:pass@23.92.23.113/mydb


    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    app.run(debug=True)