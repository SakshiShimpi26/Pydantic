from pydantic import BaseModel,Field,EmailStr,computed_field
from typing_extensions import Self

class Demo(BaseModel):
    number1 : int
    number2 : int

    # If we wanted to calculate any value based on user input we can do that using computed_fields.
    @computed_field
    @property
    def add(self)->int:
        return self.number1 + self.number2

def data_check(pydantic:Demo):
    print(pydantic.number1)
    print(pydantic.number2)
    print(pydantic.add)

data = {'number1':10,'number2':20}

object = Demo(**data)

data_check(object)