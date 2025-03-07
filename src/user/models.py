from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
import datetime

from src import Base
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
    id_subscription = Column(Integer, ForeignKey("subscription.id"), nullable=False)
    balance = Column(Float, default=0.0, nullable=False)
    avatar = Column(String(255))

    subscription = relationship("Subscription", back_populates="user")
