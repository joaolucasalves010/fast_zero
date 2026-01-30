from fastapi import FastAPI, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # Declara que o endpoint com /token será onde o usuário consiguira seu token Bearer

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]): # Depende do Bearer token no Header da requisição para funcionar
    return {"token": token}