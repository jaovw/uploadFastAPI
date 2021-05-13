from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app= FastAPI()

@app.get("/")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
	
	if published:

		return{'data': F'{limit} published posts from the DataBase'}

	else:

		return{"data":F"{limit} posts from the DataBase"}

@app.get("/unpublished")
def unpublished():
	return{'data':'all unplublished posts'}

@app.get("/comments/{id}")
def comments(id: int):
	return{'comment_id' : id}

class Blog(BaseModel):

	title: str
	body: str
	published: Optional[bool]

@app.post("/")
def create(blog: Blog):
		return{'data':F'Blog is created with title as {blog.title}'}