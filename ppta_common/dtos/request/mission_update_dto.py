from datetime import date
from typing import Optional
from pydantic import BaseModel, Field
from ...enums.contract_type_enum import ContractType
from ...enums.experience_level_enum import ExperienceLevel
from ...enums.remote_work_type_enum import RemoteWorkType
from ...enums.duration_type_enum import DurationType
from .workplace_dto import WorkplaceDto
from ...enums.mission_visibility_enum import MissionVisibility

class MissionUpdateDto(BaseModel):
    job_title: Optional[str] = Field(None, description="Title of the job")
    contract_types: Optional[list[ContractType]] = Field(None, description="Type of contracts for the mission")
    min_daily_rate: Optional[float] = Field(None, description="Min daily rate for freelance contract")
    max_daily_rate: Optional[float] = Field(None, description="max daily rate for freelance contract")
    min_annual_gross_salary: Optional[float] = Field(None, description="Min annual gross salary range")
    max_annual_gross_salary: Optional[float] = Field(None, description="Max annual gross salary range")
    is_remuneration_profile_based: Optional[bool] = Field(None, description="Indicates if remuneration is based on the profile")
    experience: Optional[ExperienceLevel] = Field(None, description="Experience level required for the mission")
    workplace: Optional[WorkplaceDto] = Field(None, description="Details about the workplace")
    start_date: Optional[date] = Field(None, description="Start date of the mission")
    starts_asap: Optional[bool] = Field(None, description="Indicates if the mission starts as soon as possible")
    type_remote_work: Optional[RemoteWorkType] = Field(None, description="Type of remote work available")
    job_description: Optional[str] = Field(None, description="Description of the job")
    skills:  Optional[dict] = Field(None, description="List of expected skills, e.g., AWS, Python, Pandas")
    know_how: Optional[dict] = Field(None, description="List of soft skills, e.g., communication, confidence")
    job:Optional[dict] =Field(None, description="The main daily activities")
    desired_profile: Optional[str] = Field(None, description="Description of the desired candidate profile")
    work_environment: Optional[str] = Field(None, description="Description of the work environment")
    company: Optional[str] = Field(None, description="ID of the company")
    created_by_company: Optional[str] = Field(None, description="ID of the company that created the mission")
    duration: Optional[int] = Field(None, ge=1, description="Duration of the mission")
    duration_type: Optional[DurationType] = Field(None, description="Duration type: DAYS, MONTHS, YEARS")
    is_renewable: Optional[bool] = Field(None, description="Indicates if the mission is renewable")
    client: Optional[str] = Field(None, description="Field for to indicate the client for this tender call")
    is_client_public: Optional[bool] = Field(False, description="the fields indicates if the client can be displayed to applicants")