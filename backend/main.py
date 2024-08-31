from fastapi import FastAPI
import motor.motor_asyncio
import pprint

from config import password # gitignored, contains password
from model import Climb
from enum import Enum

connection_string = f"mongodb+srv://admin:{password}@cluster0.6jhzc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)

app = FastAPI()

def get_db():
    return client["test_db"]

def get_climb_collection():
    db = get_db()
    collection = db["climbs"]
    return collection


@app.post("/climbs/")
async def post_climb(climb: Climb):
    document = climb.dict()
    collection = get_climb_collection()
    result = await collection.insert_one(document)
    return str(result.inserted_id)

@app.put("/climbs/{title}/{climb_id}")
async def add_id(title: str, climb_id: int):
    collection = get_climb_collection()
    old_document = await collection.find_one({"title": title})
    print("found document: %s" % pprint.pformat(old_document))
    _id = old_document["_id"]
    result = await collection.replace_one({"_id": _id}, {"climb_id": climb_id, **old_document})
    print("replaced %s document" % result.modified_count)
    new_document = await collection.find_one({"_id": _id})
    print("document is now %s" % pprint.pformat(new_document))
    return str(new_document)

@app.get("/climbs/{title}")
async def test_get(title: str):
    collection = get_climb_collection()
    result = await collection.find_one({"title": title})
    if result is None:
        result = ("404 not found")
    pprint.pprint(result)
    return str(result)


@app.put("/climbs/{climb_id}/{new_title}/")
async def change_title(climb_id: int, new_title: str):
    collection = get_climb_collection()
    result = await collection.update_one({"climb_id": climb_id}, {"$set": {"title": new_title}})
    print("updated %s document" % result.modified_count)
    new_document = await collection.find_one({"title": new_title})
    print("document is now %s" % pprint.pformat(new_document))
    return str(new_document)

@app.delete("/climbs/")
async def del_climb(title: str | None = None, climb_id: int | None = None):
    collection = get_climb_collection()
    n = await collection.count_documents({})
    print("%s documents before calling delete_one()" % n)
    if title is not None:
        result = await collection.delete_one({"title": title})
    else:
        result = await collection.delete_one({"climb_id": climb_id})
    print("%s documents after" % (n))
    return str(result)




"""
class ModelName(str, Enum):
    alexnet = "alexnet" # name: value
    resnet = "resnet"
    lenet = "lenet"
    name = "value"

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    print(model_name) # ModelName.name
    print(model_name.value) # value
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet": # "lenet" == ModelName.lenet.value
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path} # returns the file path inputted in url

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/optional")
async def option(q: str | None = None):
    if q:
        return {"q" : q}
    return {"no q"}

"""