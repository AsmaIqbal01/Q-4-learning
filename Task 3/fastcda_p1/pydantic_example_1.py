from pydantic import BaseModel, ValidationError

#Define a simple model

class User(BaseModel):
    id:int
    name:str
    email:str
    age:int | None = None #optional field with default None

#valid data

user_data = {"id":1,"name":"Alice","email":"abc@gmail.com","age":25}
user = User(**user_data)
print(user)
print(user.model_dump())

#invalid data
try:
    invalid_user = User(id="not_an_int",name="Bob",email="bob@example.com")
except ValidationError as e:
    print(e)