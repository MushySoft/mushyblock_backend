from fastapi import FastAPI
from src import Base, get_db

from src.auth import router as auth_router
from src.user import router as user_router
from src.subscription import router as subscriptions_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(subscriptions_router, prefix="/subscriptions", tags=["subscriptions"])


@app.get("/")
async def ping():
    return "pong"
