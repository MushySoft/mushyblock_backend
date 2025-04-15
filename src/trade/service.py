from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy import select

from src.trade.schemas import OfferCreate, OfferType
from src.trade.models import Item, Service


async def create_offer_db(db: AsyncSession, offer_data: OfferCreate):
    if offer_data.type not in OfferType:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid offer type: '{offer_data.type}'. Allowed types: {OfferType.__str__}"
        )

    if offer_data.type == OfferType.service:
        new_offer = Service(
            id_trade=offer_data.id_trade,
            title=offer_data.title,
            description=offer_data.description,
            price=offer_data.price,
            photo=offer_data.photo
        )

    if offer_data.type == OfferType.item:
        new_offer = Item(
            id_trade=offer_data.id_trade,
            title=offer_data.title,
            description=offer_data.description,
            price=offer_data.price,
            count=offer_data.count,
            photo=offer_data.photo
        )

    if new_offer is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to create offer. Unknown offer type."
        )
    else:
        db.add(new_offer)
        await db.commit()
        await db.refresh(new_offer)
        return {
            "message": "Offer created successfully",
            "offer_id": new_offer.id,
            "trade_id": offer_data.id_trade,
            "type": offer_data.type.value,
        }


async def get_offer_db(db: AsyncSession):
    result_service = await db.execute(select(Service))
    result_item = await db.execute(select(Item))
    return {"Services:": result_service.scalars().all(), "Items:": result_item.scalars().all()}
