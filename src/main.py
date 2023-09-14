from fastapi import FastAPI

from src.blog_service import BlogService
from src.model.request.blogpost import BlogPost as blogPost
from src.model.response.blogpost import BlogPost
from src.model.response.blogposts import BlogPosts

app: FastAPI = FastAPI()
blog_service: BlogService = BlogService()


@app.get("/")
def list_blog_posts() -> BlogPosts:
    return blog_service.get_posts()


@app.post("/blogpost")
def create_blog_post(post: blogPost) -> BlogPost:
    return blog_service.add_post(post)
