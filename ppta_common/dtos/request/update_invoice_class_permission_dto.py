from pydantic import BaseModel
from typing import Any, Dict
from ...utils.enums import FrequencyEnum, EnumRole

class UpdateInvoiceClassPermissionDto(BaseModel):
    invoice_class_id: str
    year: str
    month: str
    frequency: FrequencyEnum
    roles: list[EnumRole]

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