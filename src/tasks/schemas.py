from datetime import datetime
from typing import List
from pydantic import BaseModel, validator



def parse_passenger_date(date_str):
  
    date_obj = datetime.strptime(date_str, "%d%b%y")

    return date_obj.strftime("%Y-%m-%d")


def parse_flight_date(date_str):
  
    date_obj = datetime.strptime(date_str, "%Y%m%d")

    return date_obj.strftime("%Y-%m-%d")


class Passenger(BaseModel):
    num: str
    surname: str
    firstname: str
    bdate :str

    
    @validator("bdate")
    def validate_iso_date_format(cls, value):
        try:
            return parse_passenger_date(value)
        except ValueError:
            raise ValueError("Invalid date format, expected: YYYY-MM-DD")


class Flight(BaseModel):

    flt: int
    date: str
    dep: str
    prl: List[Passenger]

    @validator("date")
    def validate_iso_date_format(cls, value):
        try:
            return parse_flight_date(value)
        except ValueError:
            raise ValueError("Invalid date format, expected: YYYY-MM-DD")

