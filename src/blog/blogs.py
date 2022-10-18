
from fastapi import APIRouter, HTTPException
from blog.models import Blog
from auth.models import User
from typing import List
from beanie import PydanticObjectId
from blog.models import LikedBlog

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
async def get_all_likes() -> List[LikedBlog]:
    likes = await LikedBlog.find_all().to_list()
    return likes


@blog_router.post("/like", status_code=201)
async def create_likes(like: LikedBlog):
    await like.create()

    return {"message": "like was created successfully."}


@blog_router.post("/likes")
async def like(blog_id: PydanticObjectId, user_id: PydanticObjectId) -> Blog:
    print("1")
    print(blog_id)
    blog = await Blog.get(blog_id)
    user = await User.get(user_id)

    like = await LikedBlog.find(LikedBlog.blog.id == blog_id, LikedBlog.user.id == user_id, fetch_links=True).to_list()
    print(like)
    print(2)
    # like = True
    if not like:
        print(3)
        blog.like_count += 1 
        print(4)
        like.blog = blog
        like.user = user
        print(5)
        await like.save()
    else:
        print(6)
        blog.like_count -= 1
        print(7)
        await like.delete()
    print(8)
    await blog.save()
    return blog
