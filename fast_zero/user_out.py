from pydantic import BaseModel, EmailStr

class UserOut(BaseModel):
    name: str
    email: EmailStr
    full_name: str | None = None
