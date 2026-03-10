from pydantic import BaseModel
from typing import List, Dict, Optional

class Student(BaseModel):
    name:str
    age:int = 20 #default
    weight:Optional[float] = None #optional value but need to compalsory set None for Optional values
    subjects:List[str] #Here we haven't written just list because this will validate just that subjects should be list but will not validate that what types of values that list will contains.
    contact:Dict[str,str]

def student_details(pydantic:Student):
    print("============ Student Details ==============")
    print(pydantic.name)
    print(pydantic.age)
    print(pydantic.weight)
    print(pydantic.subjects)
    print(pydantic.contact)

data = {
    "name":"Sakshi Shimpi",
    "age":22,
    "subjects":["AI","Gen AI","ANN","Python"],
    "contact":{"phone":"1234567890","email":"sakshi@gmail.com"}}

object = Student(**data)

student_details(object)

