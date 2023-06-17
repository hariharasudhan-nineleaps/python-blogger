from pydantic import BaseModel


class BlogCategoryItem(BaseModel):
    id: str
    name: str