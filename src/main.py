from fastapi import FastAPI

from src.auth import router as auth_router
from src.user import router as user_router
from src.trade import router as offer_router
from src.subscription import router as subscription_router

from src import Base, get_db

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(subscription_router, prefix="/subscription", tags=["subscription"])
app.include_router(offer_router, prefix="/market", tags=["offer"])


@app.get("/")
async def ping():
    return "pong"
