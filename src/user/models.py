from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
import datetime

from src import Base
from src.subscription import Subscription
from src.trade import Trade


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(16), unique=True, nullable=False)
    email = Column(String(32), unique=True)
    hashed_password = Column(String(255), nullable=False)
    name = Column(String(16), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)
    last_login = Column(TIMESTAMP, nullable=False)
    id_subscription = Column(Integer, ForeignKey("subscription.id", name="fk_user_subscription"), unique=True)
    balance = Column(Float, default=0.0, nullable=False)
    avatar = Column(String(255))

    subscription = relationship("Subscription", uselist=False, back_populates="users")
    seller_trades = relationship("Trade", foreign_keys="[Trade.seller]", back_populates="seller_user")
    buyer_trades = relationship("Trade", foreign_keys="[Trade.buyer]", back_populates="buyer_user")