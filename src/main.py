import time
from fastapi import FastAPI
from routers import blogs, users
from database import init_db


def build_app() -> FastAPI:
    app = FastAPI(
        title="Blog List API",
        description="This is a simple API for a Blog."
    )
    app.include_router(blogs.blog_router, prefix='/blogs')
    app.include_router(users.user_router, prefix='/user')
    return app


app = build_app()


@app.on_event('startup')
async def connect():
    await init_db()

