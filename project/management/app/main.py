from fastapi import FastAPI

from .db.db import create_tables
from .routers import categories_router, notes_router, tasks_router, tags_router
from .shared.exceptions import AppExceptionCase, app_exception_handler

create_tables()

app = FastAPI()
v1 = FastAPI()

app.mount("/api/v1", v1)

v1.include_router(categories_router.router, prefix="/categories")
v1.include_router(tags_router.router, prefix="/tags")
v1.include_router(tasks_router.router, prefix="/tasks")
v1.include_router(notes_router.router, prefix="/notes")


@v1.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)
