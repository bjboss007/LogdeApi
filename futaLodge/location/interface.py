from mypy_extensions import TypedDict
from typing import List
from futaLodge.lodge.interface import LodgeInterface

class LocationInterface(TypedDict, total = False):
    id : int
    name : str
    lodges : List[LodgeInterface]
    
    