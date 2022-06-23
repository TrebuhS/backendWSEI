from fastapi import FastAPI

from .db.db import create_tables
from .routers import users_router, auth_router
from .shared.exceptions import AppExceptionCase, app_exception_handler

create_tables()

app = FastAPI()
v1 = FastAPI()

v1.include_router(users_router.router, prefix="/users")
v1.include_router(auth_router.router, prefix="/auth")

app.mount("/api/v1", v1)


@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)
