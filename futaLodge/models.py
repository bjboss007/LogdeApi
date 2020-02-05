from futaLodge import db

class Location(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), nullable =False)
  lodges = db.relationship('Lodge', backref = 'location')


class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable = True)
    contact = db.Column(db.String(16), nullable = True)
    lodges = db.relationship('Lodge', backref = 'agent') 
    
    def __repr__(self):
      return f"Agent name => '{self.name}'" 

class Lodge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable = False )
    longitude = db.Column(db.Float, nullable = False )
    name = db.Column(db.String(100), nullable =False )
    logdeinfo = db.relationship("LodgeInfo", uselist = False, backref = "lodge")
    pictures = db.relationship("Picture", backref = "lodge", lazy = True )
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'))
    
    
    def __repr__(self):
      return f"Lodge name => '{self.name}'"
    
class LodgeInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    troom = db.Column(db.String(30), nullable = True)
    num_room = db.Column(db.Integer, nullable = True)
    ammenities = db.Column(db.Text, nullable = True)
    lodge_id = db.Column(db.Integer, db.ForeignKey('lodge.id'))
    

    def __repr__(self):
      return f"Lodge name => '{self.logde_id.name}'"


   
  
class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable = True)
    lodge_id = db.Column(db.Integer, db.ForeignKey('lodge.id'))
    