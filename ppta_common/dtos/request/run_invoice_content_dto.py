import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Self

from .extended_base_model import ExtendedBaseModel
from ...enums.frequency_enum import FrequencyEnum

class RunInvoiceContentDto(ExtendedBaseModel):
    id: Optional[str] = None
    run_invoice_id: Optional[str] = None
    run_process_id: Optional[str] = None
    file_path: Optional[str] = None
    file_name: Optional[str] = None
    file_size: Optional[int] = 0
    frequency: Optional[FrequencyEnum] = None 
    file_extension: Optional[str] = None
    month: Optional[int] = 0
    year: Optional[int] = 0
    subject: Optional[str] = None
    __properties: ClassVar[List[str]] = ["id", "run_invoice_id", "invoice_received_date", "name"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
        "from_attributes": True  # mandatory
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AccountDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

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
 
    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProcessRuleDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "run_invoice_id": obj.get("run_invoice_id"),
            "run_process_id": obj.get("run_process_id"),
            "file_path": obj.get("file_path"),
            "file_name": obj.get("file_name"),
            "file_size": obj.get("file_size"),
            "frequency": obj.get("frequency"),
            "file_extension": obj.get("file_extension"),
            "month": obj.get("month"),
            "year": obj.get("year"),
            "subject": obj.get("subject"),
            "invoice_received_date": obj.get("invoice_received_date"),
            "created_at": obj.get("created_at"),
            "created_by": obj.get("created_by"),
            "updated_at": obj.get("updated_at"),
            "updated_by": obj.get("updated_by")
        })
        return _obj
