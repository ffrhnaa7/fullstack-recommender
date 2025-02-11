from typing import List,Optional
from fastapi import FastAPI, Query
from resolver import random_items, random_genres_items
# CORS stands for Cross-Origin Resource Sharing. It's a security feature 
# implemented by web browsers that controls how web pages 
# from one domain can interact with resources (such as APIs) hosted on a different domain
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/all/")
async def all_movies():
    result = random_items()
    return {"result": result}


@app.get("/genres/{genre}")
async def genre_movies(genre: str):
    result = random_genres_items(genre)
    return {"result": result}


@app.get("/user-based/")
async def user_based(params:Optional[List[str]] = Query(None)):
    return {"message": f"User based "}
@app.get("/item-based/{item_id}")
async def item_based(item_id:str):
    return {"message": f"Item based: {item_id}"}