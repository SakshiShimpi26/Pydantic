from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Student(BaseModel):
    name:str = Field(max_length=50) # check whether the length of name should not exceed 50 as length
    age:int = Field(gt=0,description="Age cant be zero or less than zero") #Field is used to add basic data validations like less than, greater than, less that equal to, etc also can data description to the specific field
    weight:Optional[float] = None 
    subjects:List[str] 
    contact:Dict[str,str]
    email:EmailStr #Built-in email validation datatype available in pydantic
    url:AnyUrl #Built-in url validation datatype - it checks whether the given url is valid or not
    lastname:Annotated[str,Field(max_length=20,title="Surname",description="Surname Field",examples=["Shimpi"])] #Field with Annotated can be used to add metadata to a specific field
    rank:Annotated[int,Field(gt=0,strict=True)] #Strict parameter supresses the behaviour of automatic type converstion like if in pydantic we pass "21" for int it directly converts to int automatically but sometimes we dont nees this behvaiour hence we can make it off using strict


def student_details(pydantic:Student):
    print("============ Student Details ==============")
    print(pydantic.name)
    print(pydantic.age)
    print(pydantic.weight)
    print(pydantic.subjects)
    print(pydantic.contact)
    print(pydantic.email)
    print(pydantic.url)
    print(pydantic.lastname)
    print(pydantic.rank)

data = {
    "name":"Sakshi Shimpi",
    "age":20,
    "subjects":["AI","Gen AI","ANN","Python"],
    "contact":{"phone":"1234567890"},
    "email":"sakshi@gmail.com",
    "url":"https://www.linkedin.com",
    "lastname":"Shimpi",
    "rank":10 #If strict parameter is set to True then by mistake if we pass "10" like this it will throw error
    }

object = Student(**data)

student_details(object)

