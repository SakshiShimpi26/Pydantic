from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
import json

app = FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Field(...,description="Id of the Patient",examples=["P001"])]
    name:Annotated[str,Field(...,description="City of the Patient")]
    city:Annotated[str,Field(...,description="City of the Patient")]
    age:Annotated[int,Field(...,description="Age of the Patient",examples=["20"],gt=0)]
    gender:Annotated[Literal['male','female','others'],Field(...,description="Gender of the Patient")]
    height:Annotated[float,Field(...,description="Height of the Patient mtrs",examples=["1.78"],gt=0)]
    weight:Annotated[float,Field(...,description="Weight of the Patient kgs",examples=["45"],gt=0)]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return "Underweight"
        elif self.bmi<30:
            return "Normal"
        elif self.bmi<60:
            return "Overweight"
        else:
            return "Obese"

# Load data from json file 
def load_data():
    with open("D:/FastAPI/02. Path and Query Parameters/patients.json",'r') as f:
        data = json.load(f)
        return data
    
def save_data(data):
    with open("D:/FastAPI/02. Path and Query Parameters/patients.json",'w') as f:
        json.dump(data,f)

@app.get("/")
def demo():
    return {"message":"Patient Management System"}

@app.get("/about")
def about():
    return {"message":"A Patient Management System Application About Section"}

@app.post("/create")
def create_patient(patient:Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient data with this ID already exists")

    data[patient.id] = patient.model_dump(exclude=[id])

    save_data(data)
        
    return JSONResponse(status_code=201, content={'message':"Patient Created Successfully"})

