from fastapi import FastAPI
from app import db, models, routes
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

app = FastAPI(title="Question Service")
app.include_router(routes.router)

@app.on_event("startup")
async def startup():
    async with db.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
