from datetime import date, datetime
from typing import List
from pydantic import BaseModel, validator



class Flight(BaseModel):

    flt: int
    dep: str
    depdate: date
    


 
