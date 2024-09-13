from typing import Any, Dict
from pydantic import BaseModel

from .professional_info_dto import ProfessionalInfoDto
from ...utils.enums import EnumUserType

class MemberDto(BaseModel):
    professional_info: ProfessionalInfoDto
    user_type:EnumUserType  

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
