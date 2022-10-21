
from typing import List

from schemas.schemas import Blog, Like

from .celery import celery_app

@celery_app.task(name="rl_task")
def reset_blog_like_count_task():
    blogs = Blog.find_all().to_list()
    likes = Like.find_all().to_list()

    for blog in blogs:
        blog.like_count = 0
        blog.save()

    for like in likes:
        like.is_active = False
        like.save()
    
    return blogs
