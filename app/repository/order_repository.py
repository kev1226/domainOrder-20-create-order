import motor.motor_asyncio
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("DB_NAME")]
collection = db["orders"]


async def save_order(order: dict):
    result = await collection.insert_one(order)
    order["id"] = str(result.inserted_id)
    return order
