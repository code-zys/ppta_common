
from typing import List, Optional, Dict, Any, ClassVar

from .extended_base_model import ExtendedBaseModel


class ProcessRuleUpdateDto(ExtendedBaseModel):
    id: Optional[str] = None
    company_id: Optional[str] = None
    run_day: Optional[str] = None
    run_month: Optional[int] = None

    next_month: Optional[int] = 0
    next_year: Optional[int] = 0
    invoice_class_ids: Optional[List[str]] = None
    override: Optional[bool] = False
    all_invoice: Optional[bool] = False
    __properties: ClassVar[List[str]] = ["id", "company_id", "run_day", "run_month", "invoice_class_ids", "all_invoice"]

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