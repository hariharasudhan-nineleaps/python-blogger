from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.exceptions import HTTPException
from fastapi import status, Depends

from src.utils.token import decode_token
from src.types.user import TokenData

auth_scheme = HTTPBearer()
async def get_current_user(credentials: Annotated[HTTPAuthorizationCredentials, Depends(auth_scheme)]) -> TokenData:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={"WWW-Authenticate": "Bearer"}
    )
    
    # read token from headers
    token = credentials.credentials

    if token is None or token == "":
        raise credentials_exception
    
    return decode_token(token)


    

    

