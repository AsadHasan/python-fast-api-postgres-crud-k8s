from pydantic import BaseModel, Field

from src.model.response.blogpost import BlogPost


class BlogPosts(BaseModel):
    blog_posts: list[BlogPost] = Field(..., alias="blogPosts")
