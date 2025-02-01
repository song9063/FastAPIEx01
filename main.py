from fastapi import FastAPI
from pydantic import BaseModel, Field, SecretStr

class User(BaseModel):
    login_id: str = Field(min_length=8, max_length=16)
    password: SecretStr = Field(exclude=True)

    name: str = Field(min_length=1, max_length=50)
    age: int = Field(gt=10, lt=150)

app = FastAPI()

@app.post("/users")
def create_user(user: User):
    return user.dict()
