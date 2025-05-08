from pydantic import BaseModel, Field
from datetime import datetime

class TransactionCreate(BaseModel):
    transaction_id: str = Field(..., min_length=1)
    user_id: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)
    currency: str = Field(..., min_length=3, max_length=3)
    timestamp: datetime

    class Config:
        orm_mode = True