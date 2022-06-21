from fastapi import FastAPI
from starlette.responses import RedirectResponse

from .db.db import create_tables
from .routers import users_router

create_tables()

app = FastAPI()
v1 = FastAPI()

v1.include_router(users_router.router, prefix="/users")

app.mount("/api/v1", v1)
