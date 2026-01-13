from pydantic import BaseModel, Field # Field -> é usado para adicionar validações opcionais e metadados em corpos BaseModel
from image import Image # Importando classe BasedModel

class Item(BaseModel):
    name: str = Field(examples=["Example name"])
    description: str | None = Field(default=None, title="The description of the item", max_length=300)
    price: float = Field(gt=0, title="The price must be greater than zero")
    tax: float | None = Field(default=None, examples=[3.2])
    # tags: list[str] = [] -> lista que aceita somente strings
    tags: set[str] = set() # -> por ser um campo tags, não pode ter valor repetido então definimos um conjunto que aceita somente tring
    # image: Image | None = None -> Modelo aninhado
    images: list[Image] | None = None # -> BaseModel como subtipo

    """
    
    model_config = { -> muda o json_schema de exemplo na documentação da API
        "json_schema_extra": {
            "example": {
                "item": {
                    "name": "Product 1",
                    "description": "Product 1 description",
                    "price": 90,
                    "tax": 30,
                    "tags": ["product", "Product_1"],
                    "images": [
                        {
                            "name": "Product 1",
                            "url": "http://localhost:8000/images/product1.png"
                        }
                    ]
                },
            }
        }
    }
    
    """


