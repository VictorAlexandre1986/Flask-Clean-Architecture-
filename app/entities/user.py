from pydantic import BaseModel, EmailStr

class UserEntity(BaseModel):
    name: str
    email: EmailStr
