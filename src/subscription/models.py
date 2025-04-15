from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import datetime

from src import Base


class Subscription(Base):
    __tablename__ = "subscription"

    id = Column(Integer, primary_key=True, index=True)
    id_subscription_type = Column(Integer, ForeignKey("subscription_type.id"), nullable=False)
    duration = Column(Integer, nullable=False)
    start_date = Column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    subscription_type = relationship("SubscriptionType", back_populates="subscriptions")
    users = relationship("User", back_populates="subscription")


class SubscriptionType(Base):
    __tablename__ = "subscription_type"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, default=0.0, nullable=False)
    photo = Column(String(255))

    subscriptions = relationship("Subscription", back_populates="subscription_type")
