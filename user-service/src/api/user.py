from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional


import httpx

from src.db import get_db
from src.utils import password
from src.utils.id import generate_unique_id
from src.models.user import User
from src.config import get_settings

from src.types.user import SignupRequestBody, LoginRequstBody, APIResponse, SignUpResponse, TokenData

from src.dependency.authentication import get_current_user

router = APIRouter(prefix='/users/api')


@router.post("/v1/signup", response_model=APIResponse[SignUpResponse, None])
async def signup(request_body: SignupRequestBody, session: AsyncSession = Depends(get_db)):
    name = request_body.name  if request_body.name else request_body.email.split('@')[0]
    db_data = {
        "id": generate_unique_id(),
        "name": name,
        "username": request_body.username,
        "email": request_body.email,
        "password_hash": password.create_password(request_body.password)
    }
    db_user = User(**db_data)
    
    async with session.begin():
        session.add(db_user)
        await session.commit()

    signup_response = SignUpResponse(**db_data, created_at=db_user.created_at)
    return APIResponse(data=signup_response, metadata=None)


@router.post("/v1/login")
async def login(request_body: LoginRequstBody, session: AsyncSession = Depends(get_db)):
    user: Optional[User] = None
    
    async with session.begin():
        stmt = select(User).where(User.email == request_body.email)
        res = await session.execute(stmt) 
        user = res.scalars().one_or_none()

        if user is None:
            raise HTTPException(status_code=401, detail="Invalid Email/Password")

    if not password.validate_password(request_body.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid Email/Password")


    async with httpx.AsyncClient(http2=True) as client:
        # config
        settings = get_settings()
        generate_auth_token_url = f'{settings.auth_service_url}/auth/api/v1/tokens/generate'

        # send req
        token_request_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "username": user.username
        }
        response = await client.post(generate_auth_token_url, json=token_request_data)
        response_data = response.json()

        # send json
        return {
            "data": {
                "access_token": response_data["data"]["access_token"]
            }
        }
    
@router.get("/v1/profile")
async def profile(token_data: Annotated[TokenData, Depends(get_current_user)]):
    return token_data