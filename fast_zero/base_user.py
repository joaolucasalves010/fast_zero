from pydantic import BaseModel, EmailStr

class BaseUser(BaseModel):
    name: str
    email: EmailStr
    full_name: str