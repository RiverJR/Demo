import logging

from db import (
    add_passenger,
    create_table,
    delete_passenger,
    delete_table,
    get_passenger,
    get_passengers,
    update_passenger,
)
from fastapi import FastAPI
from pydantic import BaseModel

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Passenger(BaseModel):
    Survived: int = None
    Pclass: int = None
    passenger_name: str = None
    Sex: str = None
    Age: int = None
    SibSp: int = None
    Parch: int = None
    Ticket: str = None
    Fare: int = None
    Cabin: str = None
    Embarked: str = None


app = FastAPI()


@app.get("/")
def root():
    return {"hello": "world"}


# Create Passenger
@app.post("/passengers")
def create_passenger_api(passenger: Passenger, passenger_id):
    return add_passenger(passenger.dict(), passenger_id)


# Lists all passengers
@app.get("/passengers")
def get_passengers_api():
    return get_passengers()


# Lists a passenger based on passenger id
@app.get("/passengers/{id}")
def get_passenger_api(id: int):
    return get_passenger(str(id))


# Update existing passengers info based on passenger id
@app.put("/passengers/{id}")
def update_passenger_api(passenger: Passenger, id: int):
    passenger_dict = passenger.dict()
    for key, value in passenger.dict().items():
        if value is None:
            del passenger_dict[f"{key}"]
    update_passenger(passenger_dict, id)
    return passenger_dict


@app.delete("/passengers/{id}")
def delete_passenger_api(id: int):
    return delete_passenger(id)


# temporary functions


@app.get("/deletetable")
def delete_table_api():
    return delete_table()


@app.get("/createtable")
def create_table_api():
    return create_table()
