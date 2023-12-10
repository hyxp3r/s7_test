import asyncio
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database import get_async_session
from flights.models import BaseFlights
from src.config import (DB_HOST_TEST, DB_NAME_TEST, DB_PASSWOR_TEST, DB_PORT_TEST,
                        DB_USER_TEST)
from src.main import app


DATABASE_URL_TEST_ASYNC = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASSWOR_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"
DATABASE_URL_TEST_SYNC = f"postgresql://{DB_USER_TEST}:{DB_PASSWOR_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

engine_test_async = create_async_engine(DATABASE_URL_TEST_ASYNC, poolclass=NullPool)
engine_test_sync = create_engine(DATABASE_URL_TEST_SYNC)

async_session_maker = sessionmaker(engine_test_async, class_=AsyncSession, expire_on_commit=False)

BaseFlights.metadata.bind = engine_test_async

async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

def override_get_sync_session():
    sync_session = sessionmaker(bind=engine_test_sync)
    session = sync_session()
    return session

app.dependency_overrides[get_async_session] = override_get_async_session


async def prepare_database():
    async with engine_test_async.begin() as conn:
        await conn.run_sync(BaseFlights.metadata.create_all)
    yield
    async with engine_test_async.begin() as conn:
        await conn.run_sync(BaseFlights.metadata.drop_all)


client = TestClient(app)

@pytest_asyncio.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac