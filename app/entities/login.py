from pydantic import BaseModel

class LoginEntity(BaseModel):
    id: int | None
    username: str
    password: str
    email: str