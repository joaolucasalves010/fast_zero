from fastapi import FastAPI

app = FastAPI(title="Estudos FastAPI")

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

# Parâmetros pré-definidos com Enum

from enum import Enum

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}
    elif model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}
    
    return {'model_name': model_name, 'message': 'Have some residuals'}

# Parâmetros de path que contêm paths
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}