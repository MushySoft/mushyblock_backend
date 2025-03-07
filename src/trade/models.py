from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src import Base
import datetime


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    id_trade = Column(Integer, ForeignKey("trade.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(255))
    count = Column(Integer, nullable=False)
    price = Column(Float, default=0.0, nullable=False)
    photo = Column(String(255))

    trade = relationship("Trade", back_populates="items")

class Trade(Base):
    __tablename__ = "trade"

    id = Column(Integer, primary_key = True, index = True)
    seller = Column(Integer, ForeignKey('user.username'))
    buyer = Column(Integer, ForeignKey('user.username'))
    status = Column(Boolean)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    finished_at = Column(TIMESTAMP)
    expires_at = Column(TIMESTAMP)

    items = relationship("Item", back_populates="trade")