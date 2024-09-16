from datetime import datetime
import json
import pprint
from typing import Any, Dict, Optional, ClassVar, List, Self

from ...enums.execution_status_enum import ExecutionStatusEnum

from ..request.extended_base_model import ExtendedBaseModel
from .process_rule_response import ProcessRuleResponse
from ..request.run_invoice_dto import RunInvoiceDto
from .user_meta_data_reponse import UserMetadataResponse
from ...enums.frequency_enum import FrequencyEnum

class RunProcessResponse(ExtendedBaseModel):
    id: str
    plan_cron: Optional[str] = None
    name: Optional[str] = None
    run_date: Optional[datetime] = None
    run_month: Optional[int] = None
    run_year: Optional[int] = None
    status: Optional[ExecutionStatusEnum] = None 
    process_rule: Optional[ProcessRuleResponse] = None
    frequency: Optional[FrequencyEnum] = None 
    run_invoice_classes: List[RunInvoiceDto] = []
    created_at: Optional[int] = None
    created_by: Optional[UserMetadataResponse] = None
    updated_at: Optional[int] = None
    updated_by: Optional[UserMetadataResponse] = None

    __properties: ClassVar[List[str]] = ["id", "plan_cron", "name",
                                         "run_date", "run_month", "run_year", "process_rule"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
        "from_attributes": True
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
            "user_id": obj.get("user_id"),
            "plan_cron": obj.get("plan_cron"),
            "name": obj.get("name"),
            "run_date": obj.get("run_date"),
            "run_month": obj.get("run_month"),
            "run_year": obj.get("run_year"),
            "process_rule": ProcessRuleResponse.model_validate(obj.get("process_rule")),
            "run_invoice_classes": [RunInvoiceDto.model_validate(run_invoice) for run_invoice in obj.get("run_invoice_classes")],
            "created_at": obj.get("created_at"),
            "created_by": UserMetadataResponse.model_validate(obj.get("created_by")),
            "updated_at": obj.get("updated_at"),
            "updated_by": UserMetadataResponse.model_validate(obj.get("updated_by")),
           
        })
        return _obj

  