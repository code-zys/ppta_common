from typing import Optional
from pydantic import BaseModel

class InvoiceOcrDto(BaseModel):
    invoice_id: Optional[str] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    va_number: Optional[str] = None
    tva_value: Optional[str] = None
    invoice_date: Optional[int] = None
    sender_name: Optional[str] = None
    sender_address: Optional[str] = None

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
        "from_attributes": True,
        "arbitrary_types_allowed": True
    }