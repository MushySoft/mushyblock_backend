from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import get_db

from src.user import service
from src.user.schemas import UserCreate, UserResponse

router = APIRouter()


@router.post("/", response_model=UserResponse)
async def register_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await service.create_user(db, user_data)
    return user
