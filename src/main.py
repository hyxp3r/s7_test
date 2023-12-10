
from contextlib import asynccontextmanager
import logging
import sys
from fastapi import Depends, FastAPI

from database import engine, create_database, create_tables
from loguru import logger
from flights.routers import router as flights_router



logger.add("app.log", format = "{time} {level} {message}", level = "INFO", )





app = FastAPI(
    title = "Test App"
   
)
app.include_router(flights_router)

@app.on_event("startup")
async def startup_db_client():
   
    await create_database()
    await create_tables()
 



