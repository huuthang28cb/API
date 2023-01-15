from random import randrange
from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
            {"title": "This is title my posts", "content": "This is my content my post, kk", "id": 1},
            {"title": "This is title my posts two", "content": "This is my content my post pizza, kk", "id": 2}
        ]
# find post with id
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

@app.get("/login")
def login():
    return {"Message": "Hello World"}

@app.get('/post')
def post():
    return {"data": my_posts}

@app.post('/addPost')
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post.dict())
    return {
        "data": post_dict
        }

# get post detail
@app.get("/post/{id}")
def post_detail(id: int):
    post = find_post(id)
    return {'post_detail': post}