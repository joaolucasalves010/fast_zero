from pydantic import BaseModel, EmailStr

class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: str
    full_name: str | None = None
