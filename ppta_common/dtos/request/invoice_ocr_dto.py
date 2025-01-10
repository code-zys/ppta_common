from typing import Any, Dict, Optional
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

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
        were set at model initialization. Other fields with value `None`
        are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict