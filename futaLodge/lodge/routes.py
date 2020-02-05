from flask import Blueprint, jsonify, request
from futaLodge.location.schemas import LocationSchema, LodgeSchema
from futaLodge.models import Location
from futaLodge.lodge.service import LodgeService
import marshmallow as mm


lodge = Blueprint('lodge', __name__)


lodge_schema = LodgeSchema()
lodge_schemas = LodgeSchema(many = True)

lodge_service = LodgeService()


@lodge.route("/api/lodge/<id>")
def get_lodge(id):
    lodge = lodge_service.get_by_id(id)
    result = lodge_schema.dump(lodge)
    return {'lodge':result}, 200