
import os

from .paths import InPath

from .file_operations import file_validate, move_file, save_json
from loguru import logger
from .database_operatons import insert_data_flights
import concurrent.futures
from functools import partial





def file_opertion_task():

    print("operation")

    files = list(filter(lambda x: x.endswith('.csv'), os.listdir(InPath)))
  
    if files:
        file = files[0]
        flight_dict = file_validate(file)
        

        if flight_dict:
            logger.info("File is valid")

            move_file(file)
            logger.info("File moved to OK")

            with concurrent.futures.ThreadPoolExecutor() as executor:
         
                save_json_partial = partial(save_json, flight_dict, file)
                insert_data_partial = partial(insert_data_flights, file=file, flight_dict=flight_dict)

              
                future_save_json = executor.submit(save_json_partial)
                future_insert_data = executor.submit(insert_data_partial)

          
                concurrent.futures.wait([future_save_json, future_insert_data])
                for future in [future_save_json, future_insert_data]:
                    if future.exception() is not None:
                        logger.error(f"Error in concurrent : {future.exception()}")

        else:
            move_file(file, False)
            logger.info("File moved to Err")

        
   


 