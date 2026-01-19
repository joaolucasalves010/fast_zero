from products import Product

from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI(title="Estudos FastAPI")

# @app.get("/")
# async def home():
#     return {"message": "Hello World"}

@app.post("/products/")
async def create_product(product: Product):
    product_dict = product.model_dump()
    if product.tax is not None:
        price_with_tax = product.price + product.tax
        product_dict['price_with_tax'] = price_with_tax
    return product_dict

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product, q: str | None = None):
    product_dict = product.model_dump()
    result = {"product_id": product_id, **product_dict}
    if q:
        result['q'] = q
    return result

from fastapi import Body
from item import Item
from user import User

# Multiplos parâmetros de corpo
# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     importance: Annotated[int, Body()],
#     item: Annotated[Item, Body(embed=True)], retorna um JSON com chave com o nome do parâmetro com o embed 
#     user: User | None = None,
#     q: str | None = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return {"item_id": item_id, "item": item, "user": user, "importance": importance}

from offer import Offer

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

from image import Image
@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    images_name = []
    for image in images:
        images_name.append(image.name)
    return images_name


from fastapi import Header
from common_headers import CommonHeaders

@app.get("/items_header/")
# async def read_items_header(user_agent: Annotated[str | None, Header()] = None): convert_underscores = False -> para de converter header snake_case para sublinhados
#     return {'user_agent': user_agent}
async def read_items_header(headers: Annotated[CommonHeaders, Header()]):
    return headers


from fastapi import Cookie
from cookie import Cookies

@app.get("/items_cookie/")
async def read_items_cookie(cookies: Annotated[Cookies, Cookie()]):
    return cookies


# Model de resposta - Tipo de retorno
items = []
@app.post("/items/")
async def create_item(item: Item) -> Item:
    items.append(item)
    return item

@app.get("/items/")
async def read_items() -> list[Item]:
    return [*items, Item(name="Portal Gun", price=42.0),Item(name="Plumbus", price=32.0)]



from fastapi import Response
from fastapi.responses import JSONResponse, RedirectResponse

@app.get("/portal/")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Você está dentro de um portal interdimensional."})


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []}
}

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True) # response_model_exclude_unset remove os parâmetros opcionais com valor null ou valores padrão
async def read_item(item_id: str):
    return items[item_id]

from user_in_db import UserInDB
from user_in import UserIn
from user_out import UserOut
from base_user import BaseUser

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password) # user_in.model_dump() transforma um objeto model em dict
    print("User saved! ..not really")
    return user_in_db

from fastapi import status
@app.post("/user/", response_model=UserOut, status_code=201) # response_model retorna o model UserOut para a rota 
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

# Dados de formulários

from fastapi import Form
from form_data import FormData

@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data

from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse

@app.post("/files/")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")] = None):
    if file is None:
        return {"message": "Not file sent"}
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: Annotated[UploadFile, File(description="A file read as UploadFile")]= None):
    if file is None:
        return {"message": "Not upload file sent"}
    return {"filename": file.filename}