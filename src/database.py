
from motor.motor_asyncio import AsyncIOMotorClient
import beanie
from schemas.schemas import Blog, User, Like


async def init_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")

    await beanie.init_beanie(
        database=client.db_name,
        document_models=[Blog, User, Like]
    )