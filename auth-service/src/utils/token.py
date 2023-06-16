from typing import Dict, Union

import jwt

def generate_token(payload: Dict[str, Union[str, int]], secret: str) -> str:
    return jwt.encode(payload, secret, algorithm="HS256")