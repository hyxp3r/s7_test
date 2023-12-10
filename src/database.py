
from typing import AsyncGenerator
from fastapi import logger
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
from flights.models import BaseFlights
import asyncpg
from sqlalchemy.orm import sessionmaker
from loguru import logger


DATABASE_URL_ASYNC = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL_ASYNC)
sync_engine = create_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

@logger.catch
async def create_database():

        connection = await asyncpg.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database='postgres' 
        )

        try:
            database_exists = await connection.fetchval(
                "SELECT 1 FROM pg_database WHERE datname = $1", DB_NAME)

            if not database_exists:
                await connection.execute(f"CREATE DATABASE {DB_NAME}")
                logger.info(f"База данных {DB_NAME} успешно создана.")
            else:
                logger.info(f"База данных {DB_NAME} уже существует.")
        
        except Exception as e:
            pass
        
        finally:
            await connection.close()
 
@logger.catch
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(BaseFlights.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


def get_sync_session():
    sync_session = sessionmaker(bind=sync_engine)
    session = sync_session()
    return session
