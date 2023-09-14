from datetime import datetime

import pytest

from src.blog_service import BlogService
from src.model.request.blogpost import BlogPost as blogPostRequest
from src.model.response.blogpost import BlogPost as blogPostResponse
from src.model.response.blogposts import BlogPosts


@pytest.fixture(scope="module")
def blog_service() -> BlogService:
    return BlogService()


def test_add_post(blog_service: BlogService):
    author: str = "Test author"
    title: str = "Test title"
    content: str = "Test content"
    created_modified_time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    request: blogPostRequest = blogPostRequest(
        author="Test author", title="Test title", content="Test content"
    )
    response: blogPostResponse = blog_service.add_post(request)
    assert response.created_date_time == created_modified_time
    assert response.last_modified_date_time == created_modified_time
    assert response.author == author
    assert response.title == title
    assert response.content == content


def test_get_post(blog_service: BlogService):
    response: BlogPosts = blog_service.get_posts()
    assert response.blog_posts
