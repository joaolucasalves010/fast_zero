from pydantic import BaseModel

# Sub-Modelo
class Image(BaseModel):
    name: str
    url: str