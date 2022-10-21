
from fastapi import APIRouter, HTTPException

from typing import List
from beanie import PydanticObjectId

from schemas.schemas import Blog, Like

blog_router = APIRouter()


@blog_router.get("/", status_code=200)
async def get_all_blogs() -> List[Blog]:
    blogs = await Blog.find_all().to_list()
    return blogs


@blog_router.post("/", status_code=201)
async def create_blogs(blog: Blog):
    await blog.create()

    return {"message": "Blog was created successfully."}

@blog_router.get("/{blog_id}", status_code=200)
async def retrive_blog(blog_id: PydanticObjectId) -> Blog:
    get_blog = await Blog.get(blog_id)

    return get_blog

@blog_router.put("/{blog_id}", status_code=200)
async def update_blog(blog_id: PydanticObjectId, blog: Blog) -> Blog:
    updated_blog = await Blog.get(blog_id)

    if not updated_blog:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )
    updated_blog.title = blog.title
    updated_blog.description = blog.description
    updated_blog.like_count = blog.like_count
    
    updated_blog.save()

    return updated_blog


@blog_router.delete("/{blog_id}", status_code=204)
async def delete_blog(blog_id: PydanticObjectId):
    deleted_blog = await Blog.get(blog_id)

    if not deleted_blog:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )
    
    await deleted_blog.delete()

    return {"message": "Blog was deleted successfully."}

@blog_router.get("/like", status_code=200)
async def get_all_likes() -> List[Like]:
    likes = await Like.find_all().to_list()
    return likes


@blog_router.post("/like", status_code=201)
async def create_likes(like: Like):
    await like.create()

    return {"message": "like was created successfully."}


@blog_router.post("/likes")
async def like(blog_id: PydanticObjectId, user_id: PydanticObjectId) -> Blog:

    blog = await Blog.get(blog_id)
    like = await Like.find_one(
        {"blog": blog_id}, 
        {"user": user_id}, 
        {"is_active": True})

    if not like:
        new_like: Like = Like(blog = blog_id, user = user_id)
        await Like.insert_one(new_like)
        
        blog.like_count += 1 

    else:
        await like.delete()
        blog.like_count -= 1
       

    await blog.save()
    return blog
