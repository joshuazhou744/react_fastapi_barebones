from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from pymongo import MongoClient
from config import password
from model import Climb

from database import (
    fetch_one_climb,
    fetch_all_climbs,
    create_climb,
    update_climb,
    remove_climb,
)

connection_string = f"mongodb+srv://admin:{password}@cluster0.6jhzc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)

app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
async def read_root():
    return {"ping":"pong"}

@app.get("/api/climb")
async def get_climb():
    response = await fetch_all_climbs()
    return response

@app.get("/api/climb{title}", response_model=Climb)
async def get_climb_by_title(title):
    response = await fetch_one_climb(title)
    if response:
        return response
    raise HTTPException(404, f"there is no climb item with the title: {title}")

@app.post("/api/climb", response_model=Climb)
async def post_climb(climb: Climb):
    response = await create_climb(climb.dict())
    if response:
        return response
    raise HTTPException(400, "something went wrong, bad request")

@app.put("/api/climb{title}", response_model=Climb)
async def put_climb(title:str, content:str):
    response = update_climb(title, content)
    if response:
        return response
    raise HTTPException(404, f"there is no climb item with the title: {title}")

@app.delete("/api/climb{title}")
async def del_climb(title):
    response = await remove_climb(title)
    if response:
        return f"Successfully removed item"
    raise HTTPException(404, f"there is no climb item with the title: {title}")


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