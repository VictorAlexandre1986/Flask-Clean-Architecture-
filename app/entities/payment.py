from pydantic import BaseModel
from typing import Datetime

class PaymentEntity(BaseModel):
    id: int | None
    id_enterprise: int
    date: Datetime
    amount: float
    type_payment: str
    status_payment: str
    transaction_id: str
    status_refund: str
    