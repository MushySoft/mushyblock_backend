from pydantic import BaseModel
from datetime import datetime
from typing import List


class SubscriptionTypeSchema(BaseModel):
    title: str
    description: str
    price: float
    photo: str | None


class SubscriptionSchema(BaseModel):
    id: int
    subscription: SubscriptionTypeSchema
    duration: int
    start_date: datetime
    status: bool
    owner: int


class SubscriptionsResponse(BaseModel):
    subscriptions: List[SubscriptionSchema]


class UserSubscriptionResponse(BaseModel):
    id: int
    subscription: SubscriptionTypeSchema
    start_date: datetime
    duration: int


class SubscriptionPurchaseRequest(BaseModel):
    subscription_id: int