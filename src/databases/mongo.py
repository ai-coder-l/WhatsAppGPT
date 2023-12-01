from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from src.config import config

client = AsyncIOMotorClient(config.MONGODB_URI)
db: AsyncIOMotorDatabase = client[config.MONGO_INITDB_DATABASE]
