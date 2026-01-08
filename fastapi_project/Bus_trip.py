from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()
class Bus_trips(BaseModel):
    id : int
    source : str
    destination : str
    fare : int

bus_trip = [
    Bus_trips(id=1,source="ahmebadabad",destination="goa",fare=15000),
    Bus_trips(id=2,source="ahmebadabad",destination="vadodra",fare=5000),
    Bus_trips(id=3,source="ahmebadabad",destination="abu",fare=1500),
    Bus_trips(id=4,source="ahmebadabad",destination="dwarka",fare=15000),
    Bus_trips(id=5,source="ahmebadabad",destination="saputara",fare=1000),
    Bus_trips(id=6,source="ahmebadabad",destination="ujain",fare=7500),
    Bus_trips(id=7,source="ahmebadabad",destination="surat",fare=7500),
    Bus_trips(id=8,source="ahmebadabad",destination="diu",fare=7500),
    Bus_trips(id=9,source="ahmebadabad",destination="kuch",fare=7500),
    Bus_trips(id=10,source="ahmebadabad",destination="rajkot",fare=7500),
    Bus_trips(id=11,source="ahmebadabad",destination="somnath",fare=7500),
            
            
            ]

@app.get("/")
def page():
    return {"message" : "welcome to tripe"}

@app.post("/trip")
def add_trips(trip : Bus_trips):
    if not trip.source.strip() or not trip.destination.strip():
    # if not trip.source or not trip.destination == None:
        raise HTTPException(status_code=400,detail="Source and destination cannot be empty")
    if trip.fare <=0:
        raise HTTPException(status_code=400,detail="fare is not zero")
    bus_trip.append(trip)
    return trip

@app.get("/trips")
def get_trips():
    if len(bus_trip) == 0:
        raise HTTPException(status_code=404,detail="trip not found")
    return bus_trip

@app.get("/trips/{trip_id}")
def get_trip(trip_id : int):
    for trip in bus_trip:
        if trip.id == trip_id:
            return trip
    raise HTTPException(status_code=404,detail="trip not found")

@app.put("/trips/{trip_id}")
def updete_trip(trip_id : int,updet_trip : Bus_trips):
    if updet_trip.fare <=0:
        raise HTTPException(status_code=400,detail="fare is not zero")
    for i in range(len(bus_trip)):
        if bus_trip[i].id == trip_id:
            bus_trip[i]=Bus_trips
            return updet_trip
    raise HTTPException (status_code=404,detail="trip not found")

@app.delete("/trips/{trip_id}")
def delete_trip(trip_id : int):
    # TODO : What if the bust_trip array is empty 
    if len(bus_trip) == 0:
        raise HTTPException(status_code=404,detail="not any trip available ")
    for i in range(len(bus_trip)):
        if bus_trip[i].id == trip_id:
            del bus_trip[i]
            return {"message" : "trip is deleted...."}
    raise HTTPException(status_code=404,detail="trip not found")

