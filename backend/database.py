from model import Climb

# MongoDB Driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.ClimbList
collection = database.climbs

async def fetch_one_climb(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_climbs():
    climbs = []
    cursor = collection.find({})
    async for document in cursor:
        climbs.append(Climb(**document))
    return climbs

async def create_climb(climb):
    document = climb
    result = await collection.insert_one(document)
    return document

async def update_climb(title, content):
    await collection.update_one({"title":title},{"$set":{
        "content":content
    }})
    document = await collection.find_one({"title":title})
    return document

async def remove_climb(title):
    await collection.delete_one({"title":title})
    return True