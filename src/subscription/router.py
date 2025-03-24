from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer

from src.database import get_db

from src.subscription.schemas import SubscriptionsResponse
from src.subscription.service import get_available_subscriptions

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/", response_model=SubscriptionsResponse)
async def get_subscriptions(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    subscriptions = await get_available_subscriptions(db)
    return subscriptions