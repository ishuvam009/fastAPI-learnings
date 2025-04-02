from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UsCred(BaseModel):
    email: str
    password: str

@app.get("/")
async def readt_root():
    return {"message":"hello"}


@app.post("/name")
async def create_name(name: str):
    return{"message": f"Hello {name}!"}

@app.post("/auth")
async def create_auth(cred: UsCred):
    authEmail = "shuvam@gmail.com"
    authPass = "1234@A"
    if(cred.email == authEmail and cred.password == authPass):
        return{"message":"Successfully logged in."}
    else:
        return{"message":"Error wrong cred."}