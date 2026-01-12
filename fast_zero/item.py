from pydantic import BaseModel, Field # Field -> é usado para adicionar validações opcionais e metadados em corpos BaseModel

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, title="The description of the item", max_length=300)
    price: float = Field(gt=0, title="The price must be greater than zero")
    tax: float | None = None