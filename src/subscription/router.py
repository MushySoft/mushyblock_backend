from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer

from src.database import get_db

from src.subscription.schemas import SubscriptionsResponse, UserSubscriptionResponse, SubscriptionPurchaseRequest
from src.subscription.service import get_available_subscriptions, purchase_subscription, get_active_subscription

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Placeholder for the user (since the user schema is not implemented yet)
fake_user_id = 1  # For example, a placeholder for a user with id = 1

@router.get("/", response_model=SubscriptionsResponse)
async def get_subscriptions(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return await get_available_subscriptions(db)


@router.post("/purchase", response_model=UserSubscriptionResponse)
async def purchase_subscription_route(
    request: SubscriptionPurchaseRequest,
    db: AsyncSession = Depends(get_db),
):
    return await purchase_subscription(fake_user_id, request.subscription_id, db)


@router.get("/active", response_model=UserSubscriptionResponse)
async def get_active_subscriptions_route(
    db: AsyncSession = Depends(get_db)
):
    return await get_active_subscription(fake_user_id, db)
