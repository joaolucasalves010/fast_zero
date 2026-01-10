from products import Product

from fastapi import FastAPI
app = FastAPI()

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