

import json
import shutil
from tasks.paths import InPath, OutPath, OkPath, ErrPath
from tasks.schemas import Passenger, Flight
import csv
from loguru import logger


def file_validate(file:str):

    try:
        date, flt, dep =  file[:-4].split("_")
    except ValueError as e:
        logger.error("File name is invalid: {e}",)
        return None


    filePath = f"{InPath}/{file}"
    passagers = []

    try:
        with open(filePath, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            for row in csv_reader:
                passagers.append(Passenger(
                            num=row['num'],
                            surname=row['surname'],
                            firstname=row['firstname'],
                            bdate=row['bdate']
                        ))
    
        flight = Flight(flt = flt, date = date, dep = dep, prl = passagers)
    except ValueError as e:
        logger.error(f"File data is not valid: {e}", )
        return None

    flight_dict = flight.model_dump()

    return flight_dict


def save_json(flight_dict:dict, file:str):


    outFile = f"{OutPath}/{file[:-4]}.json"

    try:
        with open(outFile, "w") as json_file:
            json.dump(flight_dict, json_file, indent=2)
            logger.info("File is saved to JSON")
    except Exception as e:
        logger.error("Error while saving json: {e} ", )


    return True

def move_file(file:str, ok:bool = True):
        filePath = f"{InPath}/{file}"

        if ok:
            shutil.move(filePath, OkPath)
        else:
             shutil.move(filePath, ErrPath)
             
