from sqlalchemy import Column, Text, Integer, Float, DateTime, ForeignKey
from .metadata import Base

class Equipment(Base):
    __tablename__ = 'equipments'
    id = Column(Integer, primary_key=True)
    character_id = Column(Text, ForeignKey('characters.id'))
    datetime = Column(DateTime)
    mean_item_level = Column(Float)
    head_item_id = Column(Text, nullable=True)
    head_item_quality = Column(Text, nullable=True)
    head_item_level = Column(Integer, nullable=True)
    neck_item_id = Column(Text, nullable=True)
    neck_item_quality = Column(Text, nullable=True)
    neck_item_level = Column(Integer, nullable=True)
    shoulder_item_id = Column(Text, nullable=True)
    shoulder_item_quality = Column(Text, nullable=True)
    shoulder_item_level = Column(Integer, nullable=True)
    chest_item_id = Column(Text, nullable=True)
    chest_item_quality = Column(Text, nullable=True)
    chest_item_level = Column(Integer, nullable=True)
    waist_item_id = Column(Text, nullable=True)
    waist_item_quality = Column(Text, nullable=True)
    waist_item_level = Column(Integer, nullable=True)
    legs_item_id = Column(Text, nullable=True)
    legs_item_quality = Column(Text, nullable=True)
    legs_item_level = Column(Integer, nullable=True)
    feet_item_id = Column(Text, nullable=True)
    feet_item_quality = Column(Text, nullable=True)
    feet_item_level = Column(Integer, nullable=True)
    wrist_item_id = Column(Text, nullable=True)
    wrist_item_quality = Column(Text, nullable=True)
    wrist_item_level = Column(Integer, nullable=True)
    hands_item_id = Column(Text, nullable=True)
    hands_item_quality = Column(Text, nullable=True)
    hands_item_level = Column(Integer, nullable=True)
    head_item_id = Column(Text, nullable=True)
    head_item_quality = Column(Text, nullable=True)
    head_item_level = Column(Integer, nullable=True)
    finger_1_item_id = Column(Text, nullable=True)
    finger_1_item_quality = Column(Text, nullable=True)
    finger_1_item_level = Column(Integer, nullable=True)
    finger_2_item_id = Column(Text, nullable=True)
    finger_2_item_quality = Column(Text, nullable=True)
    finger_2_item_level = Column(Integer, nullable=True)
    trinket_1_item_id = Column(Text, nullable=True)
    trinket_1_item_quality = Column(Text, nullable=True)
    trinket_1_item_level = Column(Integer, nullable=True)
    trinket_2_item_id = Column(Text, nullable=True)
    trinket_2_item_quality = Column(Text, nullable=True)
    trinket_2_item_level = Column(Integer, nullable=True)
    back_item_id = Column(Text, nullable=True)
    back_item_quality = Column(Text, nullable=True)
    back_item_level = Column(Integer, nullable=True)
    main_hand_item_id = Column(Text, nullable=True)
    main_hand_item_quality = Column(Text, nullable=True)
    main_hand_item_level = Column(Integer, nullable=True)
    off_hand_item_id = Column(Text, nullable=True)
    off_hand_item_quality = Column(Text, nullable=True)
    off_hand_item_level = Column(Integer, nullable=True)