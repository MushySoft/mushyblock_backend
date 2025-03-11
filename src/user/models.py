from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from typing import TYPE_CHECKING

from src import Base

if TYPE_CHECKING:
    from src.subscription import Subscription


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(16), unique=True, nullable=False)
    email = Column(String(32), unique=True)
    hashed_password = Column(String(255), nullable=False)
    name = Column(String(16), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)
    last_login = Column(TIMESTAMP, nullable=False)
    id_subscription = Column(Integer, ForeignKey("subscription.id", name="fk_user_subscription"), nullable=False, unique=True)
    balance = Column(Float, default=0.0, nullable=False)
    avatar = Column(String(255))

    subscription = relationship("Subscription", uselist=False, back_populates="user")
    seller_trades = relationship("Trade", foreign_keys="[Trade.seller]", back_populates="seller_user")
    buyer_trades = relationship("Trade", foreign_keys="[Trade.buyer]", back_populates="buyer_user")