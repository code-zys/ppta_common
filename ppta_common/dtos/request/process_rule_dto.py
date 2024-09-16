from __future__ import annotations

import json
import pprint
from typing import List, Optional, Self, Dict, Any, ClassVar


from .extended_base_model import ExtendedBaseModel
from ...enums.frequency_enum import FrequencyEnum


class ProcessRuleDto(ExtendedBaseModel):
    id: Optional[str] = None
    company_id: Optional[str] = None
    # plan_cron: Optional[str] = None
    # launchable_manual: Optional[bool] = False
    # name: str
    run_day: Optional[str] = None
    run_month: Optional[int] = None
    next_month: Optional[int] = 0
    next_year: Optional[int] = 0
    frequency: Optional[FrequencyEnum] = None 
    invoice_class_ids: Optional[List[str]] = None
    all_invoice: Optional[bool] = False
    override: Optional[bool] = False
    __properties: ClassVar[List[str]] = ["id", "company_id", "run_day", "run_month", "frequency",
                                         "invoice_class_ids", "all_invoice"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
        "from_attributes": True,
        "arbitrary_types_allowed": True
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
            "company_id": obj.get("company_id"),
            "run_day": obj.get("run_day"),
            "run_month": obj.get("run_month"),
            "frequency": obj.get("frequency"),
            "invoice_class_ids": obj.get("invoice_class_ids"),
            "all_invoice": obj.get("all_invoice"),
            "override": obj.get("override"),
            # "launchable_manual": obj.get(" launchable_manual")
        })
        return _obj