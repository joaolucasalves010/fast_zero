from fastapi import FastAPI, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

from pydantic import BaseModel, EmailStr

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # Declara que o endpoint com /token será onde o usuário consiguira seu token Bearer

class User(BaseModel):
    username: str
    email: EmailStr | None = None
    full_name: str | None = None
    disabled: bool | None = None

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user

@app.get("/users/me")
async def read_user_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]): # Depende do Bearer token no Header da requisição para funcionar
    return {"token": token}