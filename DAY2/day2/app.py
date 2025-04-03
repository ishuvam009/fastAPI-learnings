from fastapi import FastAPI
from pydantic import BaseModel
from .middleware import TokenAuthMiddleware

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

class DataRequest(BaseModel):
    data: str
    query: str

valid_token  = "567ss7qw8VHVHvhjhvHVNVjj785dVjhvjhj67GhhEYnjfds"

valid_username = "shuvam@gmail.com"
valid_password = "12345@Aa"

app.add_middleware(TokenAuthMiddleware, valid_token=valid_token)

@app.post("/user")
async def check_user(user_data: User):
    if user_data.username == valid_username and user_data.password == valid_password:
        return{"message":"Login Success.",
               "token":valid_token}
    else:
        return{"message":"Error"}
    
@app.post("/data")
async def income_data(userData: DataRequest):
    a = userData.data
    b = userData.query
    c = " "
    d = a + c + b

    return{"message":d}
