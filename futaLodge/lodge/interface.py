from mypy_extensions import TypedDict


class LodgeInterface(TypedDict, total = False):
    id: int
    latitude : float
    longitude : float
    name : str
    location_id : int
    
    
class LodgeInfoInterface(TypedDict, total = False):
    id : int
    troom : str
    num_room : int 
    amenities : str
    lodge_id : int
    

class AgentInterface(TypedDict, total = False):
    name: str
    contact : str
