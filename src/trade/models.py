from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Boolean, ForeignKey, Enum
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


class Service(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True, index=True)
    id_trade = Column(Integer, ForeignKey("trade.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0.0, nullable=False)
    photo = Column(String(255))

    trade = relationship("Trade", back_populates="services")


class Trade(Base):
    __tablename__ = "trade"

    id = Column(Integer, primary_key=True, index=True)
    seller = Column(Integer, ForeignKey("user.id"), nullable=False)
    buyer = Column(Integer, ForeignKey("user.id"))
    description = Column(String(255))
    status = Column(Enum("moderate", "active", "finished", name="status_enum"), nullable=False, default="moderate")
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)
    finished_at = Column(TIMESTAMP)
    expires_at = Column(TIMESTAMP, nullable=False)

    seller_user = relationship("User", foreign_keys=[seller], back_populates="seller_trades")
    buyer_user = relationship("User", foreign_keys=[buyer], back_populates="buyer_trades")    
    items = relationship("Item", back_populates="trade")
    services = relationship("Service", back_populates="trade")