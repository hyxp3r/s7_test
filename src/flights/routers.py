
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from .models import Flights
from sqlalchemy import select
from datetime import date
from .schemas import Flight

router = APIRouter (
    prefix= "/flights",
    tags=["Flights"]

)


@router.get("/", response_model=List[Flight])
async def get_flights(depdate: date, offset:int = 0, limit:int =10, session: AsyncSession = Depends(get_async_session)):
    query = select(Flights.flt, Flights.dep, Flights.depdate).where(Flights.depdate == depdate)
    result = await session.execute(query)
    return result.mappings().all()[offset:][:limit]





