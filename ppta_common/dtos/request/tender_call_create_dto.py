from datetime import date
from typing import Optional
from pydantic import BaseModel, Field
from ...enums.contract_type_enum import ContractType
from ...enums.remote_work_type_enum import RemoteWorkType
from ...enums.experience_level_enum import ExperienceLevel
from ...enums.duration_type_enum import DurationType
from .workplace_dto import WorkplaceDto

class TenderCallCreateDto(BaseModel):
    job_title: str = Field(..., description="Title of the job")
    reference: str = Field(..., description="Reference identifier for the tender call")
    contract_types: list[ContractType] = Field(..., description="Type of contracts for the tender call")
    min_daily_rate: Optional[float] = Field(None, description="Daily min rate range for freelance contracts ")
    max_daily_rate: Optional[float] = Field(None, description="Daily max rate range for freelance contracts ")
    max_annual_gross_salary: Optional[int] = Field(None, description="Annual gross salary range a max")
    min_annual_gross_salary: Optional[int] = Field(None, description="Annual gross salary range a max")
    is_remuneration_profile_based: bool = Field(..., description="Indicates if remuneration is based on the profile")
    experience: ExperienceLevel = Field(..., description="Experience level required for the tender call")
    workplace: WorkplaceDto = Field(..., description="Details about the workplace")
    start_date: Optional[date] = Field(None, description="Start date of the tender call")
    starts_asap: bool = Field(..., description="Indicates if the tender call starts as soon as possible")
    type_remote_work: RemoteWorkType = Field(..., description="Type of remote work available")
    job_description: str = Field(..., description="Description of the job")
    skills:  Optional[dict] = Field(None, description="List of expected skills, e.g., AWS, Python, Pandas")
    know_how: Optional[dict] = Field(None, description="List of soft skills, e.g., communication, confidence")
    desired_profile: str = Field(..., description="Description of the desired candidate profile")
    work_environment: str = Field(..., description="Description of the work environment")
    duration: Optional[int] = Field(None, ge=1, description="Duration of the tender call")
    duration_type: Optional[DurationType] = Field(None, description="Duration type: DAYS, MONTHS, YEARS")
    is_renewable: bool = Field(False, description="Indicates if the tender call is renewable")
    job:Optional[dict] =Field(None, description="The main daily activities")
    is_final: Optional[bool] = Field(False, description="Indicates if tender call should be marked as unpublished or maintained as draft after creation")
    final_client: Optional[str] = Field(None, description="Field for to indicate the final client for this tender call")
    is_client_public: Optional[bool] = Field(False, description="the fields indicates if the client can be displayed to applicants")
    is_client_recruiter: bool = Field(True, description="Indicates if the client is the recruiter for the tender call")