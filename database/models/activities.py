from sqlalchemy import Column, Text, DateTime, Integer, ForeignKey
from .metadata import Base


class Activity(Base):
    __tablename__ = 'activities'
    
    id = Column(Integer, primary_key=True)
    activity_id = Column(Text)
    type = Column(Text)
    name = Column(Text)
    character_id = Column(Text, ForeignKey("characters.id"), nullable=True)
    datetime = Column(DateTime)
