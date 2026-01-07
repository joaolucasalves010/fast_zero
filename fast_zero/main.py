from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Olá Mundo!"}

# Parâmetro com tipagem
@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {"item_id": item_id}

# Parâmetros devem ser definidos em ordem.

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "The current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}



@app.get('/users')
async def read_users():
    return ['Rick Sanchez', 'Morty']

# @app.get('/users')
# async def read_users2():
#     return ['Spongebob', 'Patrick']

"""
Não é possível retornar valores diferentes em uma mesma rota

A primeira definida sempre sera usada

"""