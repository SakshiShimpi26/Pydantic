from pydantic import BaseModel,Field,EmailStr,field_validator,model_validator
from typing import List, Dict,Annotated
from typing_extensions import Self

class Employee(BaseModel):
    name:str
    email:EmailStr
    age:int
    contact:Dict[str,str]

    # If we wanted to validate and check more than single field as field_validator then we use model_validator
    @model_validator(mode="after")
    def check(self):
        if self.age >= 60 and 'emergency' not in self.contact:
            raise ValueError("Employee > 60 must have emergency contact")
        return self

def data_check(pydantic:Employee):
    print(pydantic.name)
    print(pydantic.email)
    print(pydantic.age)
    print(pydantic.contact)

data = {"name":"Sakshi","email":"sakshi@hdfc.com","age":67,"contact":{'phone':"123457",'emergency':"726829397"}}

object = Employee(**data)

data_check(object)