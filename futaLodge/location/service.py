
from futaLodge.models import Location
from .interface import LocationInterface
from typing import List
from futaLodge import db

class LocationService():
    
    @staticmethod
    def get_all() -> List[Location]:
        return Location.query.all()
    
    @staticmethod
    def get_by_id(location_id: int) -> Location:
        return Location.query.get_or_404(location_id)
    
    @staticmethod
    def update(location: Location) -> Location:
        location = location
        db.session.add(location)
        db.session.commit()
        return location
    
    @staticmethod
    def create(new_attrs: LocationInterface) -> Location:
        new_location = Location(
            name = new_attrs["name"]
        )       
        db.session.add(new_location)
        db.session.commit()
        
        return new_location 
    
        
    