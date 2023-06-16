from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException, Response
import base64

from typing import Annotated

from src.types.auth import GenerateTokenRequestBody, GenerateTokenResponse, APIResponse, ExchangeTokenResponse
from src.config import Settings, get_settings
from src.utils.token import generate_token as generate_jwt_token

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


auth_scheme = HTTPBearer()
router = APIRouter(prefix='/auth/api')


@router.post("/v1/tokens/generate", response_model=APIResponse[GenerateTokenResponse, None])
async def generate_token(request_body: GenerateTokenRequestBody, settings: Annotated[Settings, Depends(get_settings)]):
    access_token = generate_jwt_token(request_body.dict(), settings.jwt_secret)
    access_token = str(base64.b64encode(bytes(access_token, encoding='utf-8')), encoding='utf-8')
    response_data = GenerateTokenResponse(access_token=access_token)

    return APIResponse(data=response_data, metadata=None)


@router.post("/v1/tokens/exchange", response_model=APIResponse[ExchangeTokenResponse, None])
async def exchange_token(response: Response, creds: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    try:
        access_token = f"Bearer {str(base64.b64decode(creds.credentials), encoding='utf-8')}"
        response_data = ExchangeTokenResponse(access_token=access_token)
        response.headers['Authorization'] = access_token
        return APIResponse(data=response_data, metadata=None)
    except KeyError:
        return HTTPException(401, detail='Unauthenticated.')