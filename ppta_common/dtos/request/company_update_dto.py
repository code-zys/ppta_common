from pydantic import BaseModel
from typing import Any, Dict, Optional
from .address_dto import AddressDto
from .timezone_dto import TimezoneDto
from ...enums.company_type_enum import CompanyType

class CompanyUpdateDto(BaseModel):
    id: Optional[str] = None
    siret: Optional[str]
    name: Optional[str]
    activity: Optional[str]
    type: Optional[CompanyType] = None
    timeZone: Optional[TimezoneDto] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[AddressDto] = None
    billing_email : Optional[str]= None
    currency : Optional[str]= None
    billing_address : Optional[AddressDto] = None
    use_contact_as_billing_info : Optional[bool] = True
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