from pydantic import BaseModel

class BankTransactionPricingDto(BaseModel):
    currency: str
    value: float