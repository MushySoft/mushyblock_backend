from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List


class SubscriptionTypeSchema(BaseModel):
    title: str = Field(max_length=255)
    description: str = Field(max_length=255)
    price: float = Field(default=0.0)
    photo: Optional[str] = Field(None, max_length=255)


class SubscriptionSchema(BaseModel):
    id: int
    subscription: SubscriptionTypeSchema
    duration: int
    start_date: datetime
    status: bool = Field(default=True)
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