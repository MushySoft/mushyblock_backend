from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload, selectinload
from datetime import datetime

from src.user import models as user_models

from src.subscription.models import SubscriptionType, Subscription


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


async def purchase_subscription(user_id: int, subscription_id: int, db: AsyncSession):
    subscription_type = await db.execute(
        select(SubscriptionType).where(SubscriptionType.id == subscription_id)
    )
    subscription_type = subscription_type.scalars().first()

    if not subscription_type:
        raise ValueError("Subscription type not found")

    new_subscription = Subscription(
        id_subscription_type = subscription_id,
        duration = 30, #?
        start_date = datetime.utcnow(),
        status = True
    )

    user = await db.execute(select(user_models.User).where(user_models.User.id == user_id))
    user = user.scalars().first()

    if not user:
        raise ValueError("User not found")

    db.add(new_subscription)
    await db.commit()
    await db.refresh(new_subscription)

    user.id_subscription = new_subscription.id
    await db.commit()
    await db.refresh(user)

    return {
        "id": new_subscription.id,
        "subscription": {
            "title": subscription_type.title,
            "description": subscription_type.description,
            "price": subscription_type.price,
            "photo": subscription_type.photo,
        },
        "duration": new_subscription.duration,
        "start_date": new_subscription.start_date,
    }


async def get_active_subscriptions(user_id: int, db: AsyncSession):
    async with db.begin():
        result = await db.execute(
            select(Subscription)
            .options(selectinload(Subscription.subscription_type))
            .filter(Subscription.users.any(user_models.User.id == user_id), Subscription.status == True)
        )
        
        subscriptions = result.scalars().all()
        
        active_subscriptions = [
            {
                "subscription_id": subscription.id,
                "subscription": {
                    "title": subscription.subscription_type.title,
                    "description": subscription.subscription_type.description,
                    "price": subscription.subscription_type.price,
                    "photo": subscription.subscription_type.photo,
                },
                "duration": subscription.duration,
                "start_date": subscription.start_date,
            }
            for subscription in subscriptions
        ]
        
        return active_subscriptions
