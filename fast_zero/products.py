from pydantic import BaseModel

"""

Criando e importando BaseModel Product

"""

class Product(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None