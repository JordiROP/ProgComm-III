from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    user_id: int
    id: Optional[int] = None
    title: str
    body: Optional[str] = None

@app.get("/users")
def get_all():
    return [User(user_id=1, id=1, title='user1_id_1', body='descr_1_1'), User(user_id=1, id=2, title='user1_id_2', body='descr_1_2'), 
            User(user_id=1, id=3, title='user1_id_3', body='descr_1_3'), User(user_id=2, id=1, title='user2_id_1', body='descr_2_1'), 
            User(user_id=2, id=2, title='user2_id_2', body='descr_2_2'), User(user_id=3, id=3, title='user3_id_3', body='descr_3_3'),
            User(user_id=3, id=1, title='user2_id_1', body='descr_2_1'), User(user_id=3, id=2, title='user2_id_2', body='descr_2_2'), 
            User(user_id=3, id=3, title='user3_id_3', body='descr_3_3')]

@app.get("/users/{user_id}")
async def get_filter(user_id:int):
    users = [User(user_id=1, id=1, title='user1_id_1', body='descr_1_1'), User(user_id=1, id=2, title='user1_id_2', body='descr_1_2'), 
             User(user_id=1, id=3, title='user1_id_3', body='descr_1_3'), User(user_id=2, id=1, title='user2_id_1', body='descr_2_1'),
             User(user_id=2, id=2, title='user2_id_2', body='descr_2_2'), User(user_id=3, id=3, title='user3_id_3', body='descr_3_3'),
             User(user_id=3, id=1, title='user2_id_1', body='descr_2_1'), User(user_id=3, id=2, title='user2_id_2', body='descr_2_2'),
             User(user_id=3, id=3, title='user3_id_3', body='descr_3_3')]
    return [user for user in users if user.user_id == user_id]

@app.post("/users/")
async def post_user(user: User):
    return user

@app.put("/users/")
async def update_user(user: User):
    return user

@app.patch("/users/")
async def patch_user(user: User):
    return user

@app.delete("/users/{user_id}")
async def delete_suer(user_id: int):
    return {'user_id': user_id}