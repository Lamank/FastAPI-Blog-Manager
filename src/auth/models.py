from datetime import datetime
from beanie import Document
from pydantic import Field


class User(Document):
    username: str = Field(max_length=16, min_length=8)
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