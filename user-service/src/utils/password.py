import bcrypt
from typing import Optional


def create_password(plain_password: str, salt: Optional[str] = None) -> str:
    if salt is None:
        salt = bcrypt.gensalt(12)
    
    hashed_password =  bcrypt.hashpw(bytes(plain_password, 'utf-8'), salt)

    return str(hashed_password, 'utf-8')

def validate_password(plain_password: str, hashed_password: str) -> bool:
    plain_password_bytes = bytes(plain_password, 'utf-8')
    hashed_password_bytes = bytes(hashed_password, 'utf-8')
    return bcrypt.checkpw(plain_password_bytes, hashed_password_bytes)