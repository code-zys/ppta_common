from typing import Optional
from pydantic import BaseModel, validator

class InvoiceClassDto(BaseModel):
    supplier: str
    name: str
    description: Optional[str] = ""
    
    @validator("supplier")
    def validate_supplier(cls, value):
            if not value:
                raise ValueError("supplier ne peut pas être vide")
            return value
    
    @validator("name")
    def validate_name(cls, value):
            if not value:
                raise ValueError("name ne peut pas être vide")
            return value