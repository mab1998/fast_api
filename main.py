from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
    name: str
    imageUrl: str = None
    jsondata: str
    status: str = None

# @app.post("/templat")
# async def root(name,imageUrl,jsondata,status):
#     return {"message": "Hello World"}

@app.post("/templat/")
async def create_item(item: Item):
    return item