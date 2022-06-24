from fastapi import FastAPI

from .db.db import create_tables
from .routers import auth_router, users_router, friends_router
from .shared.exceptions import AppExceptionCase, app_exception_handler

create_tables()

app = FastAPI()
v1 = FastAPI()

app.mount("/api/v1", v1)

v1.include_router(users_router.router, prefix="/tasks")
v1.include_router(friends_router.router, prefix="/tasks/categories")

v1.include_router(auth_router.router, prefix="/auth")



@v1.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)
