from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from iso4217 import Currency
from .total_dto import TotalDto

class InvoiceOcrDto(BaseModel):
    invoice_id: Optional[str] = None
    currency: Optional[Currency] = None
    invoice_date: Optional[datetime] = None
    sender_name: Optional[str] = None
    sender_address: Optional[str] = None
    total: Optional[TotalDto] = None
    pricing: Optional[dict] = None
    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
        "from_attributes": True,
        "arbitrary_types_allowed": True
    }