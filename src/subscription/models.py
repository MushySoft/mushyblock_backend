from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship
from src import Base
import datetime


class Subscription(Base):
    __tablename__ = "subscription"

    id = Column(Integer, primary_key=True, index=True)
    subscription = Column(Integer, nullable=False, ForeignKey("subscription_type.id"))
    duration = Column(Integer, nullable=False)
    start_date = Column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)
    status = Column(Boolean, nullable=False)

    subscription_type = relationship("SubscriptionType", back_populates="subscription")



class SubscriptionType(Base):
    __tablename__ = "subscription_type"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    subscription = relationship("Subscription", back_populates="subscription_type")
    