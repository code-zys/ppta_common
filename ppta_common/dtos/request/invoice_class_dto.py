from typing import Optional
from pydantic import BaseModel, validator
from ...enums.role_enum import EnumRole

class InvoiceClassDto(BaseModel):
    id: Optional[str] = None
    supplier: str
    name: str
    description: Optional[str] = ""
    only_visible_by = Optional[list[EnumRole]] = []
    can_upload = Optional[list[EnumRole]] = []

    
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