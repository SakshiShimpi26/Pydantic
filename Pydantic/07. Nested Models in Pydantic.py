from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pincode : str

class Employee(BaseModel):
    name:str
    age:int
    address:Address

address_data = {"city":"Pune","state":"Maharashtra","pincode":"412207"}

address_object = Address(**address_data)

employee_data = {"name":"Sakshi","age":22,"address":address_data}

employee_data = Employee(**employee_data)

print(employee_data.name)
print(employee_data.age)
print(employee_data.address)