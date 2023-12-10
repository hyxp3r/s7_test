from datetime import datetime
from database import get_sync_session
from sqlalchemy.ext.asyncio import AsyncSession
from flights.models import Flights
from sqlalchemy import insert
from loguru import logger

@logger.catch
def insert_data_flights(file: str, flight_dict: dict, session = None):

    file_name = file[:-4]
    flt = flight_dict["flt"]
    depdate = datetime.strptime(flight_dict["date"], '%Y-%m-%d')
    dep = flight_dict["dep"]

    if session is None:
        session =  get_sync_session()

    with session.begin():
        stmt = insert(Flights).values(file_name=file_name, flt=flt, depdate=depdate, dep=dep)
        session.execute(stmt)
        session.commit()
        logger.info("Sucessfully insert in DB")
    
