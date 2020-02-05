from futaLodge import ma
from marshmallow import fields as fl
from marshmallow import INCLUDE
from futaLodge.models import Location, Lodge, LodgeInfo



class AgentSchema(ma.Schema):
    class Meta:
        fields = ('name','contact')
        unknown  = INCLUDE
     
    __links = ma.Hyperlinks(
        {
            "self": ma.URLFor("agent.get_agent", id="<id>"),
            "collection": ma.URLFor("agent.get_all_agent"),
            "lodges": ma.URLFor("agent.get_agent_lodges", agent_id = "<id>")
        }
    )
    