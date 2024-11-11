from pydantic import BaseModel 
from typing import Datetime

class LoginDTO(BaseModel):
    id: int | None
    date: Datetime
    photo: str
    id_user: int
    total_hours: float
    pause : bool