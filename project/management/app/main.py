from fastapi import FastAPI

from .db.db import create_tables
from .routers import categories_router
from .shared.exceptions import AppExceptionCase, app_exception_handler

create_tables()

app = FastAPI()
v1 = FastAPI()

app.mount("/api/v1", v1)

v1.include_router(categories_router.router, prefix="/categories")


@v1.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)
