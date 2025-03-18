from pydantic import BaseModel

class ApplicationCreateDto(BaseModel):
    mission_id: str
    message: str
    applied_for_consultant_id: str
    cv: Optional[str] = ""
    contract_type: str
    min_daily_rate: Optional[float] = 0
    max_daily_rate: Optional[float] = 0
    min_annual_gross_salary: Optional[float] = 0
    max_annual_gross_salary: Optional[float] = 0