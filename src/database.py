
from motor.motor_asyncio import AsyncIOMotorClient
import beanie
from blog.models import Blog, LikedBlog
from auth.models import User


async def init_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")

    await beanie.init_beanie(
        database=client.db_name,
        document_models=[Blog, User, LikedBlog]
    )