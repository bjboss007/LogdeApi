from flask import Blueprint, jsonify, request
from futaLodge.location.schemas import LocationSchema
from futaLodge.agent.schema import AgentSchema
from futaLodge.lodge.schema import LodgeSchema
from futaLodge.models import Location, Lodge
from futaLodge.lodge.service import LodgeService
from .service import LocationService
import marshmallow as mm


api = Blueprint('api', __name__, url_prefix="/api")

locationSchemas = LocationSchema(many = True)
locationSchema = LocationSchema()

lodge_schema = LodgeSchema()
lodge_schemas = LodgeSchema(many = True)
agent_schemas = AgentSchema(many = True)
agent_schema = AgentSchema()

location_service = LocationService()

lodge_service = LodgeService()



@api.route("/locations")
def get_location():
    locations  = location_service.get_all()
    result = locationSchemas.dump(locations)
    return {"locations":result}, 200

@api.route("/locations/<int:id>")
def get_location_detail(id):
    location = location_service.get_by_id(id)
    result = locationSchema.dump(location)
    return result, 200

@api.route("/locations", methods = ["POST"])
def save_location():
    req = request.get_json(force= True)
    data = locationSchema.load(req)
    location = location_service.create(data)
    result = locationSchema.dump(location)
    return result, 201

@api.route("/locations/<id>/lodges", methods = ["POST"])
def add_lodge(id):
    data = request.get_json(force= True)
    lodge_sc = lodge_schema.load(data)
    lodge_sc['location_id'] = id
    re_lodge_sc = lodge_service.create(lodge_sc)    
    result = lodge_schema.dump(re_lodge_sc)
    return result, 201 

@api.route("/locations/<location_id>/lodges")
def get_location_lodges(location_id):
    lodges = location_service.get_by_id(location_id).lodges
    result = lodge_schemas.dump(lodges)
    return {"lodges":result}, 200

@api.route("/lodges/<id>")
def get_lodge(id):
    lodge = Lodge.query.get(1)
    result = lodge_schema.dump(lodge)
    return result, 200

@api.route("/agents")
def add_agents():
    data = request.get_json(force= True)
    agent_schema = agent_schema.load(data)

