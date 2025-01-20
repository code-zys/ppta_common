from datetime import date
from typing import List, Optional, Tuple
from pydantic import BaseModel, Field, root_validator
from ...enums.contract_type_enum import ContractType
from ...enums.remote_work_type_enum import RemoteWorkType
from ...enums.experience_level_enum import ExperienceLevel
from ...enums.duration_type_enum import DurationType
from .workplace_dto import WorkplaceDto

class MissionCreateDto(BaseModel):
    job_title: str = Field(..., description="Title of the job")
    reference: str = Field(..., description="Reference identifier for the mission")
    contract_type: ContractType = Field(..., description="Type of contract for the mission")
    min_daily_rate: float = Field(..., description="Min daily rate for freelance contract")
    max_daily_rate: float = Field(..., description="max daily rate for freelance contract")
    min_annual_gross_salary: float = Field(..., description="Min annual gross salary range")
    max_annual_gross_salary: float = Field(..., description="Max annual gross salary range")
    is_remuneration_profile_based: bool = Field(..., description="Indicates if remuneration is based on the profile")
    experience: ExperienceLevel = Field(..., description="Experience level required for the mission")
    workplace: WorkplaceDto = Field(..., description="Details about the workplace")
    start_date: Optional[date] = Field(None, description="Start date of the mission")
    starts_asap: bool = Field(..., description="Indicates if the mission starts as soon as possible")
    type_remote_work: RemoteWorkType = Field(..., description="Type of remote work available")
    job_description: str = Field(..., description="Description of the job")
    expected_skills: List[str] = Field(..., description="List of expected skills, e.g., AWS, Python, Pandas")
    know_how: List[str] = Field(..., description="List of soft skills, e.g., communication, confidence")
    desired_profile: str = Field(..., description="Description of the desired candidate profile")
    work_environment: str = Field(..., description="Description of the work environment")
    company: str = Field(..., description="ID of the company")
    created_by_company: Optional[str] = Field(None, description="ID of the company that created the mission")
    duration: int = Field(..., ge=1, description="Duration of the mission")
    duration_type: DurationType = Field(..., description="Duration type: DAYS, MONTHS, YEARS")
    is_renewable: bool = Field(False, description="Indicates if the mission is renewable")