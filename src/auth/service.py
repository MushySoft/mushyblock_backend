import requests
from fastapi import HTTPException, status
from src.auth.security import verify_password

USER_SERVICE_URL = "http://user-service/api/v1/users"


async def authenticate_user(username: str, password: str):
    response = requests.get(f"{USER_SERVICE_URL}/{username}")

    if response.status_code != 200:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    user = response.json()
    if not verify_password(password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return user
