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

class Trade(Base):
    __tablename__ = "trade"
    id = Column(Integer, primary_key = True, index = True)
    seller = Column(Integer, ForeignKey('user.username'))
    buyer = Column(Integer, ForeignKey('user.username'))
    status = Column(Boolean)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    finished_at = Column(TIMESTAMP)
    expires_at = Column(TIMESTAMP)
    offer = Column(Integer, ForeignKey('offer.id'))
