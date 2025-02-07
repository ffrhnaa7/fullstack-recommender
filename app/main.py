from typing import List,Optional
from fastapi import FastAPI, Query

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/all/")
async def all_movies():
    return {"message": "All movies"}
@app.get("/genres/{genre}")
async def genre_movies(genre:str):
    return {"message": f"Movies in genre: {genre}"}
@app.get("/user-based/")
async def user_based(params:Optional[List[str]] = Query(None)):
    return {"message": f"User based "}
@app.get("/item-based/{item_id}")
async def item_based(item_id:str):
    return {"message": f"Item based: {item_id}"}