from datetime import datetime

from src.model.request.blogpost import BlogPost as blogPostRequest
from src.model.response.blogpost import BlogPost as blogPostResponse
from src.model.response.blogposts import BlogPosts


class BlogService:
    def __init__(self):
        self._posts: list[blogPostResponse] = []

    def add_post(self, post_request: blogPostRequest) -> blogPostResponse:
        dt_format: str = "%Y-%m-%d %H:%M:%S"
        created_modified_time = datetime.now().strftime(dt_format)
        post_response: blogPostResponse = blogPostResponse(
            **{
                **post_request.model_dump(),
                **{
                    "createdDateTime": created_modified_time,
                    "lastModifiedDateTime": created_modified_time,
                },
            }
        )
        self._posts.append(post_response)
        return post_response

    def get_posts(self) -> BlogPosts:
        return BlogPosts(blogPosts=self._posts)
