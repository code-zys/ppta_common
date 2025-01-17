from datetime import date
from typing import List, Optional
from pydantic import BaseModel, root_validator
from ...enums.contract_type_enum import ContractType
from ...enums.remote_work_type_enum import RemoteWorkType
from ...enums.experience_level_enum import ExperienceLevel

class MissionDTO(BaseModel):
    job_title: str
    reference: str
    contract_type: ContractType
    daily_rate: Optional[float] = None
    annual_gross_salary: Optional[tuple[int, int]] = None
    is_remuneration_profile_based: bool
    experience: ExperienceLevel
    workplace: dict
    start_date: Optional[date] = None
    starts_asap: bool
    type_remote_work: RemoteWorkType
    job_description: str
    expected_skills: List[str]
    know_how: List[str]
    desired_profile: str
    work_environment: str

    class Config:
        use_enum_values = True

    @root_validator
    def validate_salary_range(cls, values):
        """
        Ensure salary range is valid if provided.
        """
        salary_range = values.get("annual_gross_salary")
        if salary_range:
            min_salary, max_salary = salary_range
            if min_salary <= 0 or max_salary <= 0 or min_salary > max_salary:
                raise ValueError("Invalid salary range. Ensure values are positive and min <= max.")
        return values