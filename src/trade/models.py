from sqlalchemy import Column, VARCHAR, Integer, String, Float, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src import Base
import datetime


class Offer(Base):
    tablename = "offer"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(VARCHAR(16), nullable=False)
    description = Column(VARCHAR(255))
    item = Column(Integer)
    owner = Column(Integer, ForeignKey('user.id'))

    item1 = relationship("Item")
    trade = relationship("Trade")

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(255), nullable=False)
    count = Column(Integer, nullable=False)
    price = Column(Float, default=0.0)

