from typing import Dict, Union

import jwt


from src.types.user import TokenData

def decode_token(token: str) -> TokenData:
    decoded_token: Dict[str, Union[str, int]] = jwt.decode(token, options={"verify_signature": False}) 
    return TokenData(**decoded_token)
