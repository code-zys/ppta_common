from typing import List, Optional
from pydantic import BaseModel
from ppta_common.enums.language_level_enum import EnumLanguageLevel
from ppta_common.dtos.request.address_dto import AddressDto
from ppta_common.dtos.request.timezone_dto import TimezoneDto
from ppta_common.dtos.request.workplaces_dto import WorkPlaceCreationDto


class LanguageDto(BaseModel):
    code: str
    titled: str
    level: EnumLanguageLevel

class BasicSkill(BaseModel):
    name: str
    description: Optional[str] = None


class CoachCreationDto(BaseModel):
    name: str
    email: str
    phone: str
    years_of_experience: int
    languages: List[LanguageDto] = []
    min_booking_time: Optional[int] = None
    is_coaching_profile_visible: bool = True
    bio: Optional[str] = None
    address: Optional[AddressDto] = None
    profile_picture: Optional[str] = None
    job_title: Optional[str] = None
    timezone: Optional[TimezoneDto] = None

    mission_support: Optional[bool] = False
    mission_workplace: Optional[List[WorkPlaceCreationDto]] = None
    mission_another_pricing: Optional[float] = None
    mission_default_pricing: Optional[float] = None

    interview_support: Optional[bool] = False
    interview_workplace: Optional[List[WorkPlaceCreationDto]] = None
    interview_another_pricing: Optional[float] = None
    interview_default_pricing: Optional[float] = None

    communication_support: Optional[bool] = False
    communication_description: Optional[str] = None
    communication_another_pricing: Optional[float] = None
    communication_default_pricing: Optional[float] = None

    it_support: Optional[bool] = False
    it_skills: Optional[List[BasicSkill]] = None
    it_another_pricing: Optional[float] = None
    it_default_pricing: Optional[float] = None

    other_support: Optional[bool] = False
    other_title: Optional[str] = None
    other_description: Optional[str] = None
    other_another_pricing: Optional[float] = None
    other_default_pricing: Optional[float] = None