from pydantic import BaseModel, EmailStr

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None