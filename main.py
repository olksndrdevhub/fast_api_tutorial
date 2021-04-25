from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return {
        'data': {'name': 'Oleksandr'}
    }


@app.get('/about')
def about():
    return {
        'data': 'about page'
    }


@app.get('/blog')
def blog(limit: int = 10, published: bool = True, sort: Optional[str]=None):

    if published:
        return {
            'data': f'blog list with limit = {limit} of published posts'
        }
    elif published == False:
         return {
            'data': f'blog list with limit = {limit} of unpublished posts'
        }


@app.get('/blog/unpablished')
def unpublished():
    return {
        'data': 'unpablished posts'
    }


@app.get('/blog/{id}')
def show_post(id: int):
    # or do smth with this variable
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit: int = 10):
    # fetch comments of blog with id=id
    return limit
    return {'data': {'1', '2'}}


# models

class Post(BaseModel):
    title: str
    body: str
    published: Optional[bool]




# POST methods
@app.post('/blog')
def create_post(post: Post):
    return {
        'data': f'Post is created with next data {post}'
    }



# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=9000)

