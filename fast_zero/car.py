from pydantic import BaseModel

class Car(BaseModel):
    model: str
    brand: str
    year: int
