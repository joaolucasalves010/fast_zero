from pydantic import BaseModel, Field # Field -> é usado para adicionar validações opcionais e metadados em corpos BaseModel
from image import Image # Importando classe BasedModel

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, title="The description of the item", max_length=300)
    price: float = Field(gt=0, title="The price must be greater than zero")
    tax: float | None = None
    # tags: list[str] = [] -> lista que aceita somente strings
    tags: set[str] = set() # -> por ser um campo tags, não pode ter valor repetido então definimos um conjunto que aceita somente tring
    # image: Image | None = None -> Modelo aninhado
    images: list[Image] | None = None # -> BaseModel como subtipo