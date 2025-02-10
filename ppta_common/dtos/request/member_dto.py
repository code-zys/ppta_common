from typing import Any, Dict
from pydantic import BaseModel
from .professional_info_dto import ProfessionalInfoDto
from ...utils.enums import EnumUserType
from pydantic import BaseModel, Field
from typing import Optional

class MemberDto(BaseModel):
    professional_info: Optional[ProfessionalInfoDto] = Field(None, description="List of expected skills, e.g., AWS, Python, Pandas")
    user_type: Optional[EnumUserType] = Field(..., description="List of expected skills, e.g., AWS, Python, Pandas")
    key_skills: dict = Field(..., description="List of expected skills, e.g., AWS, Python, Pandas")
    general_skills: Optional[dict] = Field(None, description="List of expected skills, e.g., AWS, Python, Pandas")
    know_how: Optional[dict] = Field(None, description="List of expected skills, e.g., AWS, Python, Pandas")
    job: Optional[dict] = Field(None, description="The main daily activities")
    cv: Optional[str] = Field(None, description="The s3 key of the cv of the member")
    other_cvs: list[str] = Field(None, description="The other cv(s) of the member")
    photo: Optional[str] = Field(None, description="The s3 key of the picture of the member")
    departments: list[str] = Field(..., description="The list of departments were the member can work")
    min_average_daily_rate: float = Field(..., description="Min dailly rate ")
    max_average_daily_rate: float = Field(..., description="Min dailly rate ")
    availability_date: int = Field( ..., description="The availability date of the member")

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
            exclude={},
            exclude_none=True,
        )
        return _dict