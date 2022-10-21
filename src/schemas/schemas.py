from datetime import datetime
from beanie import Document, PydanticObjectId
from pydantic import Field

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

class Like(Document):
    blog: PydanticObjectId
    user: PydanticObjectId
    is_active: bool = True

    class Settings:
        name = "Like_database"


class User(Document):
    username: str = Field(max_length=16, min_length=2)
    email: str
    password: str = Field(max_length=20, min_length=8)
    created_at: datetime = datetime.now()

    class Settings:
        name = "User_database"

    class Config:
        schema_extra={
            "username": "username",
            "email": "username@gmail.com",
            "password": "password"
        }