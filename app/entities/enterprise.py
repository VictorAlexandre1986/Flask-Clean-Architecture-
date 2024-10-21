from pydantic import BaseModel, EmailStr

class EnterpriseEntity(BaseModel):
    id: int | None
    name: str
    email: EmailStr
    phoneNumber: str
    id_login: int
    address: str
    city: str
    state: str
    cep: str
    number: str
    complement: str
    cnpj: str
    status: bool
    id_user: int | None