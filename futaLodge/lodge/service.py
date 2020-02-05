from .interface import LodgeInterface
from futaLodge.models import Lodge, LodgeInfo
from futaLodge import db




class LodgeService():
    
    @staticmethod
    def get_all():
        return Lodge.query.all()
    
    @staticmethod
    def get_by_id(int: id):
        lodge = Lodge.query.get_or_404(id)
        return lodge
    
    @staticmethod
    def update(id):
        lodge = lodge.query.get_or_404(id)
        if lodge:
            db.session.commit()
        return lodge
    
    @staticmethod
    def create(new_attr: LodgeInterface) -> Lodge:
        new_lodge = Lodge(
            location_id = new_attr['location_id'],
            latitude = new_attr['latitude'],
            longitude = new_attr['longitude'],
            name = new_attr['name']
            
        )
        
        db.session.add(new_lodge)
        db.session.commit()
        
        return new_lodge
    
    @staticmethod
    def create_with_id(id) -> Lodge:
        lodge = self.get_by_id(id)
        lodge.location_id = id
        db.session.commit()
        
        return lodge