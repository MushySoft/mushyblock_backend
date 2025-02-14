from sqlalchemy import Column, Integer, String, Float, TIMESTAMP
from sqlalchemy.orm import relationship
from src import Base
import datetime


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(12), unique=True, nullable=False)
    email = Column(String(16), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    name = Column(String(12), nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    last_login = Column(TIMESTAMP, nullable=True)
    balance = Column(Float, default=0.0)

    # # Связи
    # subscriptions = relationship("Subscription", back_populates="owner")
    # player = relationship("Player", uselist=False, back_populates="user")
