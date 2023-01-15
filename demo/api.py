from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"hello": "world"}


# Create Passenger
@app.post("/passengers")
def create_passenger():
    return {"status": "success"}


# Lists all passengers
@app.get("/passengers")
def titanic_results():
    return {"Passengers": "Here"}


# Lists a passenger based on passenger id
@app.get("/passengers/{id}")
def titanic_id(id: int):
    return {"Passenger": id}


# Update existing passengers info based on passenger id
@app.put("/passengers/{id}")
def update_passenger(id: int):
    return {("Passenger.%s", id): "Updated"}


@app.delete("/passengers/{id}")
def delete_passenger(id: int):
    return {("Passenger.%s", id): "Deleted"}
