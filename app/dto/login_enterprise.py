from pydantic import BaseModel, EmailStr

class LoginEnterpriseDTO(BaseModel):
    id: int | None
    username: str
    password: str
    email: EmailStr
    