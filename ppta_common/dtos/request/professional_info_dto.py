
from datetime import date
from typing import Any, Dict
from pydantic import BaseModel


class ProfessionalInfoDto(BaseModel):
    work_station: str
    phone_number: str
    professional_email: str
    start_date: date

    
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