from sqlalchemy import Column, Text
from .metadata import Base

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Text, primary_key=True)
    server = Column(Text)
    name = Column(Text)
    _class = Column(Text, name="class")
    race = Column(Text)
    faction = Column(Text)
    gender = Column(Text)
