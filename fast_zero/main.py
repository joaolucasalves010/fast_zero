from products import Product

from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI(title="Estudos FastAPI")

@app.get("/")
async def home():
    return {"message": "Hello World"}

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
@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    importance: Annotated[int, Body()],
    item: Annotated[Item, Body(embed=True)], # retorna um JSON com chave com o nome do parâmetro com o embed 
    user: User | None = None,
    q: str | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return {"item_id": item_id, "item": item, "user": user, "importance": importance}

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

from fastapi import Cookie

@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id} # retorna null