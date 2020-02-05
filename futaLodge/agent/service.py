from .interface import AgentInterface
from futaLodge.models import Agent
from futaLodge import db




class AgentService():
    
    @staticmethod
    def get_all():
        return Agent.query.all()
    
    @staticmethod
    def get_by_id(int: id):
        lodge = Agent.query.get_or_404(id)
        return lodge
    
    @staticmethod
    def update(id):
        agent = Agent.query.get_or_404(id)
        if agent:
            db.session.commit()
        return agent
    
    @staticmethod
    def create(new_attr: AgentInterface) -> Agent:
        new_agent = Agent(
            name = new_attr['name'],
            contact = new_attr['contact'],        
        )
        db.session.add(new_agent)
        db.session.commit()
        return new_agent
    
    
    @staticmethod
    def delete(id):
        agent = Agent.query.get_or_404(id)
        if agent:
            db.session.delete()
        return agent
    