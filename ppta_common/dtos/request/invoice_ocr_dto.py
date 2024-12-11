from typing import Optional

class InvoiceOcrDto():
    invoice_id: Optional[str] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    va_number: Optional[str] = None
    tva_value: Optional[str] = None
    invoice_date: Optional[int] = None
    sender_name: Optional[str] = None
    sender_address: Optional[str] = None