from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.trade.schemas import OfferCreate
from src.trade.service import create_offer_db
from src import get_db


router = APIRouter()


@router.post("/offer/create", description="создать офер типа item или service")
async def create_offer(offer_data: OfferCreate, db: AsyncSession = Depends(get_db)):
    return await create_offer_db(db, offer_data)