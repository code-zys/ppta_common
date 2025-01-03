from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from iso4217 import Currency

class InvoiceOcrDto(BaseModel):
    invoice_id: Optional[str] = None
    total_amount: Optional[float] = None
    currency: Optional[Currency] = None
    tva_number: Optional[str] = None
    tva_value: Optional[str] = None
    invoice_date: Optional[datetime] = None
    sender_name: Optional[str] = None
    sender_address: Optional[str] = None

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
        "from_attributes": True,
        "arbitrary_types_allowed": True
    }