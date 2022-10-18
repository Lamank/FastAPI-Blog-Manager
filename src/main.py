
from fastapi import FastAPI
from blog.blogs import blog_router
from auth.tasks import user_router
from database import init_db

def build_application():
    app = FastAPI(
        title="Blog List API",
        description="This is a simple API for a Blog."
    )

    return app


app = build_application()

@app.on_event('startup')
async def connect():
    await init_db()

app.include_router(blog_router, prefix='/blogs')
app.include_router(user_router, prefix='/user')
