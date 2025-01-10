from pydantic import BaseModel

class TotalDto(BaseModel):
    vat_value: float = 0.0
    vat_percent: float = 0.0
    ttc: float = 0.0
    ht: float = 0.0