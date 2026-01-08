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


# Parâmetros de consulta
fake_books_db = [{"book_id": 1, "book_name": "Harry Potter"}, {"book_id": 2, "book_name": "Ice And Fire"}, {"book_id": 3, "book_name": "Grokking Algorithms"}]

@app.get("/books/")
async def read_book(book_id: int | None = None, book_name: str | None = None, q: bool | None = False):
    for book in fake_books_db:
        if book_id is not None and book_id == book["book_id"]:
            if not q:
                return {"book_id": book['book_id'], "book_name": book['book_name']}
            else:
                return {"book_id": book['book_id'], "book_name": book['book_name'], "description": f"{book['book_name']} is a nice book, have a long description"}
        elif book_name is not None and book_name == book['book_name']:
            if not q:
                return {"book_id": book['book_id'], "book_name": book['book_name']}
            else:
                return {"book_id": book['book_id'], "book_name": book['book_name'], "description": f"{book['book_name']} is a nice book, have a long description"}
            
    return "Book not found"

# Corpo da requisição
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/products/")
async def create_product(product: Product):
    product_dict = product.model_dump()
    if product.tax is not None:
        price_with_tax = product.price + product.tax
        product_dict['price_with_tax'] = price_with_tax
    return product_dict

@app.put("/producrs/{product_id}")
async def update_product(product_id: int, product: Product, q: str | None = None):
    product_dict = product.model_dump()
    result = {"product_id": product_id, **product_dict}
    if q:
        result['q'] = q
    return result