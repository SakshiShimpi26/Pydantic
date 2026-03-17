from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pincode : str

class Employee(BaseModel):
    name:str
    age:int
    gender:str = "Female"
    address:Address

address_data = {"city":"Pune","state":"Maharashtra","pincode":"412207"}

address_object = Address(**address_data)

employee_data = {"name":"Sakshi","age":22,"address":address_data}

employee_data = Employee(**employee_data)

print(employee_data.name)
print(employee_data.age)
print(employee_data.address)

# Serialization is the process of exporting pydantic object in JSON or Dict form

# Exporting in Dict
data1 = employee_data.model_dump()
print(data1)
print(type(data1))

# Exporting in JSON
data2 = employee_data.model_dump_json()
print(data2)
print(type(data2))

# Extra methods options for serialization
# Exporting in Dict
# Include --> decides which parameters should be included in the export file
data = employee_data.model_dump(include=['name'])
print(data)
print(type(data))

# Exporting in Dict
# Exclude --> decides which parameters should be excluded from the export file
data = employee_data.model_dump(exclude=['address'])
print(data)
print(type(data)) 

# Exclude Unset --> excludes the values that are dynamically set during run time
# In this case gender will be excluded as it was set during runtime and we havent passed it during object initialization.
data = employee_data.model_dump(exclude_unset=True)
print(data)
print(type(data))