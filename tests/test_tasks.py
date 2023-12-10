import pytest
import os
from src.tasks.file_operations import file_validate, save_json, move_file
from pathlib import Path

InPath = Path(__file__).resolve().parent.parent / "src" / "flights" / "media" / "In"
OutPath = Path(__file__).resolve().parent.parent / "src" / "flights" / "media" / "Out"
OkPath = Path(__file__).resolve().parent.parent / "src"/ "flights" / "media" / "Ok"
ErrPath = Path(__file__).resolve().parent.parent / "src" / "flights" / "media" / "Err"

@pytest.fixture
def example_file():
  
    example_file_path = InPath / "20221129_1234_DME.csv"
    with open(example_file_path, "w") as f:
        f.write("num;surname;firstname;bdate\n1;IVANOV;IVAN;11NOV73\n2;PETROV;ALEXANDER;13JUL79\n3;BOSHIROV;RUSLAN;12APR78\n")
    yield example_file_path
 
 

def test_file_validate(example_file):
    result = file_validate(os.path.basename(example_file))
    print(result)
    assert result is not None 


def test_save_json(example_file):
  
    flight_dict = {"flt": "flight", "date": "2023-12-11", "dep": "dep", "prl": []}
    result = save_json(flight_dict, os.path.basename(example_file))
    assert result is True  


def test_move_file(example_file):
 
    flight_dict = {"flt": "flight", "date": "2023-12-11", "dep": "dep", "prl": []}
    save_json(flight_dict, os.path.basename(example_file))

    move_file(os.path.basename(example_file), ok=True)

    assert os.path.exists(OkPath / os.path.basename(example_file))

