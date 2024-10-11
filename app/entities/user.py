from pydantic import BaseModel, EmailStr

class UserEntity(BaseModel):
    id: int | None
    name: str
    email: EmailStr
    photo: str
    phoneNumber: str
    id_login: int
