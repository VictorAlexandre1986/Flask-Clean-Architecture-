from pydantic import BaseModel, EmailStr

class LoginDTO(BaseModel):
    id: int | None
    username: str
    password: str
    email: str
    