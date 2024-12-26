from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class PatchUser(BaseModel):
    user_id: int
    id: Optional[int] = None
    title: Optional[str] = None
    body: Optional[str] = None

class User(BaseModel):
    user_id: int
    id: int
    title: str
    body: str

    def update_user(self, patch_user: PatchUser):
        if patch_user.id:
            self.id = patch_user.id

        if patch_user.title:
            self.title = patch_user.title

        if patch_user.body:
            self.body = patch_user.body

class PostUsers(BaseModel):
    users: list = []

post_users = PostUsers()

@app.get("/users")
def get_all():
    return [User(user_id=1, id=1, title='user1_id_1', body='descr_1_1'), User(user_id=1, id=2, title='user1_id_2', body='descr_1_2'), 
            User(user_id=1, id=3, title='user1_id_3', body='descr_1_3'), User(user_id=2, id=1, title='user2_id_1', body='descr_2_1'), 
            User(user_id=2, id=2, title='user2_id_2', body='descr_2_2'), User(user_id=3, id=3, title='user3_id_3', body='descr_3_3'),
            User(user_id=3, id=1, title='user2_id_1', body='descr_2_1'), User(user_id=3, id=2, title='user2_id_2', body='descr_2_2'), 
            User(user_id=3, id=3, title='user3_id_3', body='descr_3_3')]

@app.get("/users/partial")
def get_some(limit:int, skip:int):
    return [User(user_id=1, id=1, title='user1_id_1', body='descr_1_1'), User(user_id=1, id=2, title='user1_id_2', body='descr_1_2'), 
            User(user_id=1, id=3, title='user1_id_3', body='descr_1_3'), User(user_id=2, id=1, title='user2_id_1', body='descr_2_1'), 
            User(user_id=2, id=2, title='user2_id_2', body='descr_2_2'), User(user_id=3, id=3, title='user3_id_3', body='descr_3_3'),
            User(user_id=3, id=1, title='user2_id_1', body='descr_2_1'), User(user_id=3, id=2, title='user2_id_2', body='descr_2_2'), 
            User(user_id=3, id=3, title='user3_id_3', body='descr_3_3')][skip:][:limit]

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
    post_users.users.append(user)
    return post_users.users

@app.put("/users/")
async def update_user(user: User):
    post_users.users = [old_user for old_user in post_users.users 
                        if user.user_id != old_user.user_id]
    post_users.users.append(user)
    return post_users.users

@app.patch("/users/")
async def patch_user(user: PatchUser):
    to_update_user: User = [old_user for old_user in post_users.users if user.user_id == old_user.user_id][0]
    to_update_user.update_user(user)
    return post_users

@app.delete("/users/{user_id}")
async def delete_suer(user_id: int):
    post_users.users = [user for user in post_users.users if user_id != user.user_id]
    return {'user_id': user_id}