from pydantic import BaseModel, Field


class BlogPost(BaseModel):
    author: str = Field(..., max_length=50)
    title: str = Field(..., max_length=100)
    content: str = Field(..., max_length=2000)
