from fastapi import FastAPI

from .api.ping import router as ping_router
from .api.user import router as user_router
from .models.user import User
from .db import engine

app = FastAPI(docs_url='/users/api/docs', openapi_url='/users/openapi.json')
app.include_router(ping_router)
app.include_router(user_router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)
