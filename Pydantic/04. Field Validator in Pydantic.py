from pydantic import BaseModel,Field,EmailStr
from typing import List, Dict,Annotated

class Employee(BaseModel):
    name:str
    email:EmailStr
    age:int
    
    # Here if we wanted to check whether the Employee belongs to HDCF or BOB bank then in its email we can check that
    # To implete this we can use field validator in pydantic to validate whether its from HDFC or BOB bank
    @field_validator('email')
    @classmethod
    def email_check(cls,value):
        s = value.split("@")[-1]
        if s == "hdfc.com":
            return "HDFC Employee"
        elif s == "bob.com":
            return "BOB Employee"
        else:
            raise ValueError("Not a employee of any bank HDFC and BOB")
    
    # If we everytime wants to convert the name of employee to capital case we can do that as well
    @field_validator('name')
    @classmethod
    def name_capitalize(cls,value):
        return value.upper()
    
    # mode=after --> after type conversion when input occurs [DEFAULT]
    # mode=before --> before type conversion when input occurs
    @field_validator('age',mode="after")
    @classmethod
    def mode_check(cls,value):
        return type(value)

def data_check(pydantic:Employee):
    print(pydantic.name)
    print(pydantic.email)
    print(pydantic.age)

data = {"name":"Sakshi","email":"sakshi@hdfc.com","age":'22'}

object = Employee(**data)

data_check(object)