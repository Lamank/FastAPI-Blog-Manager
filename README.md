# Blog API

This is a simple CRUD app for blogs

## Endpoints

### Blog API
- GET /blogs get_all_blogs
- POST /blogs create_blog
- Get /blogs/{blog_id} retrive_blog
- Put /blogs/{blog_id} update_blog
- Delete /blogs/{blog_id} delete_task

### User API
- GET /user get_all_users
- POST /user create_user


## Celery
At the end of the day, blog likes are reset with "Celery".