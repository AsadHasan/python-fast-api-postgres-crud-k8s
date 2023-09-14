from pydantic import BaseModel, Field

from src.model.request.blogpost import BlogPost as blogPost


class BlogPost(blogPost, BaseModel):
    created_date_time: str = Field(..., alias="createdDateTime")
    last_modified_date_time: str = Field(..., alias="lastModifiedDateTime")
