from futaLodge import ma
from marshmallow import fields as fl
from marshmallow import INCLUDE
from futaLodge.agent.schema import AgentSchema

class LodgeSchema(ma.Schema):
    class Meta:
        fields = ('id','latitude','longitude','name','location_id','_links')
        unknown = INCLUDE
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("api.get_lodge", id="<id>"), 
            "collection" : ma.URLFor("api.get_location_lodges", location_id = "<location_id>")
        }
    )
    latitude = fl.Float()
    longitude = fl.Float()
    

class LodgeInfoSchema(ma.Schema):
    class Meta:
        fields = ('troom', 'num_room', 'amenities','lodge_id', 'agent')

    agent = fl.Nested(AgentSchema)
    