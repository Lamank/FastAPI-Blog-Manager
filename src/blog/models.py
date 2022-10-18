from datetime import datetime
from beanie import Document, Link
from pydantic import Field
from auth.models import User

class Blog(Document):
    title: str = Field(min_length=2, max_length=256)
    description: str = Field(title="The description of blog", min_length=1)
    like_count: int = 0
    date_created: datetime = datetime.now()

    class Settings:
        name = "Blog_database"

    class Config:
        schema_extra={
            "title": "Blog title",
            "description": "The description of blog",
            "like_count": 3,
            "date_created": datetime.now()
        }

class LikedBlog(Document):
    blog: Link[Blog] 
    user: Link[User]

    class Settings:
        name = "Liked_blog_database"
