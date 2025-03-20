from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import requests
from datetime import timedelta

from src.auth.service import authenticate_user
from src.auth.security import create_access_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=timedelta(minutes=60))
    return {"access_token": access_token, "token_type": "bearer"}
