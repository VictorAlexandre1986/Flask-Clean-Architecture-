from pydantic import BaseModel, EmailStr

class LoginEnterpriseEntity(BaseModel):
    id: int | None
    username: str
    password: str
    email: EmailStr