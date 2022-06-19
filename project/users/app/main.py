from fastapi import FastAPI
from .routers import users_router

app = FastAPI()
v1 = FastAPI()

v1.include_router(users_router.router, prefix="/users")

app.mount("/api/v1", v1)
