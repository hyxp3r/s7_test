from sqlalchemy import  Integer, String,  Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  mapped_column

BaseFlights = declarative_base()


class Flights(BaseFlights):

    __tablename__ = "flights"

    id = mapped_column("id", Integer, primary_key = True)
    file_name  = mapped_column("file_name", String , nullable = False)
    flt    = mapped_column("flt", Integer , nullable = False)
    depdate  = mapped_column("depdate", Date , nullable = False)
    dep  = mapped_column("dep", String , nullable = False)