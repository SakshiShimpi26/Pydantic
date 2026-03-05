from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

# Load data from json file 
def load_data():
    with open("D:/FastAPI/02. Path and Query Parameters/patients.json",'r') as f:
        data = json.load(f)
        return data

@app.get("/")
def demo():
    return {"message":"Patient Management System"}

@app.get("/about")
def about():
    return {"message":"A Patient Management System Application About Section"}

# Showing the user data to user
@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patients/{patient_id}")
def view_patient_by_id(patient_id:str= Path(...,description="Unique ID for the Patient",example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient Data Not Found")

@app.get("/sort")
def sort_patients(sort_by : str = Query(...,description="Columns name by which data should be sorted",example="height"),
                  order : str = Query(description="Ascending or descending",example="asc or desc")):
    
    values_for_sort = ['height','weight','bmi']
    if sort_by not in values_for_sort:
        raise HTTPException(status_code=404,detail="Sort column not supported values should be heightm weight or bmi")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=404,detail="No such supported order for sorting. Supported order should be asc or desc")
    
    data = load_data()

    if order:
        if order == 'asc':
            flag = False
        else:
            flag = True

    sorted_data = sorted(data.values(), key= lambda x: x.get(sort_by,0),reverse=flag)
    
    return sorted_data
    

    