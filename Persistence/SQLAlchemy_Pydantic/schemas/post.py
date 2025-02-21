from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    user_id: int

class PostResponse(PostBase):
    id: int

    class Config:
        orm_mode = True
