from pydantic import BaseModel

class TokenData(BaseModel):
    id: str
    name: str
    username: str
    email: str

    class Config:
        extra = 'ignore'

    @property
    def user_id(self):
        return self.id