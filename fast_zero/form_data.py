from pydantic import BaseModel

class FormData(BaseModel):
    username: str
    password: str
    model_config = {'extra': 'forbid'}