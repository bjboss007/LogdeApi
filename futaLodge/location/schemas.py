from futaLodge import ma
from marshmallow import fields as fl
from marshmallow import INCLUDE
from futaLodge.lodge.schema import LodgeSchema



class LocationSchema(ma.Schema):
    class Meta:
        fields = ('id','name','lodges','_links')
        unknown = INCLUDE
    _links = ma.Hyperlinks(
        {   "self": ma.URLFor("api.get_location_detail", id="<id>"),
            "collection": ma.URLFor("api.get_location"),
            "lodges": ma.URLFor("api.get_location_lodges", location_id = "<id>")
         }
    )
    lodges = fl.Nested(LodgeSchema, many=True)

