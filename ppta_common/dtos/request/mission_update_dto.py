from datetime import date
from typing import List, Optional, Tuple
from pydantic import BaseModel, Field
from ...enums.contract_type_enum import ContractType
from ...enums.experience_level_enum import ExperienceLevel
from ...enums.remote_work_type_enum import RemoteWorkType
from ...enums.duration_type_enum import DurationType
from .workplace_dto import WorkplaceDto

class MissionUpdateDto(BaseModel):
    job_title: Optional[str] = Field(None, description="Title of the job")
    reference: Optional[str] = Field(None, description="Reference identifier for the mission")
    contract_type: Optional[ContractType] = Field(None, description="Type of contract for the mission")
    daily_rate: Optional[Tuple[float, float]] = Field(None, description="Daily rate range for freelance contracts as a tuple (min, max)")
    annual_gross_salary: Optional[Tuple[int, int]] = Field(None, description="Annual gross salary range as a tuple (min, max)")
    is_remuneration_profile_based: Optional[bool] = Field(None, description="Indicates if remuneration is based on the profile")
    experience: Optional[ExperienceLevel] = Field(None, description="Experience level required for the mission")
    workplace: Optional[WorkplaceDto] = Field(None, description="Details about the workplace")
    start_date: Optional[date] = Field(None, description="Start date of the mission")
    starts_asap: Optional[bool] = Field(None, description="Indicates if the mission starts as soon as possible")
    type_remote_work: Optional[RemoteWorkType] = Field(None, description="Type of remote work available")
    job_description: Optional[str] = Field(None, description="Description of the job")
    expected_skills: Optional[List[str]] = Field(None, description="List of expected skills, e.g., AWS, Python, Pandas")
    know_how: Optional[List[str]] = Field(None, description="List of soft skills, e.g., communication, confidence")
    desired_profile: Optional[str] = Field(None, description="Description of the desired candidate profile")
    work_environment: Optional[str] = Field(None, description="Description of the work environment")
    company: Optional[str] = Field(None, description="ID of the company")
    created_by_company: Optional[str] = Field(None, description="ID of the company that created the mission")
    duration: Optional[int] = Field(None, ge=1, description="Duration of the mission")
    duration_type: Optional[DurationType] = Field(None, description="Duration type: DAYS, MONTHS, YEARS")
    is_renewable: Optional[bool] = Field(None, description="Indicates if the mission is renewable")