

from mypy_extensions import TypedDict
from typing import List
from futaLodge.lodge.interface import LodgeInterface


class AgentInterface(TypedDict, total = False):
    id: int
    name: str
    contact: str
    lodges : List[LodgeInterface]
    
    