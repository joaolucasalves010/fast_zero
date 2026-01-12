from pydantic import BaseModel, HttpUrl

# Sub-Modelo
class Image(BaseModel):
    name: str
    url: HttpUrl # Valida se a string passada é uma url válida