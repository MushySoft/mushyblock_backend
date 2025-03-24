from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from datetime import datetime

from src.subscription.models import Subscription


async def get_available_subscriptions(db: AsyncSession):
    result = await db.execute(
        select(Subscription)
        .options(
            joinedload(Subscription.subscription_type),
            joinedload(Subscription.users)
        )
    )
    subscriptions = result.unique().scalars().all()

    return {
        "subscriptions": [
            {
                "id": sub.id,
                "subscription": {
                    "title": sub.subscription_type.title,
                    "description": sub.subscription_type.description,
                    "price": sub.subscription_type.price,
                    "photo": sub.subscription_type.photo,
                },
                "duration": sub.duration,
                "start_date": sub.start_date,
                "status": sub.status,
                "owner": sub.users.id
            }
            for sub in subscriptions
        ]
    }
