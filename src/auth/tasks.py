
from fastapi import APIRouter, HTTPException
from auth.models import User
from typing import List

user_router = APIRouter()

@user_router.post('/', status_code=201)
async def create_user(user: User):
    await user.create()

    return {"message": "User created successfully."}


@user_router.get('/', status_code=200)
async def get_user() -> User:
    users = await User.find_all().to_list()

    return users


