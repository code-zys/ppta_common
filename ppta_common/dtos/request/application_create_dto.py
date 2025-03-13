from pydantic import BaseModel

class ApplicationCreateDto(BaseModel):
    message: str
    cv: str
    mission_id: str
    applied_for_consultant_id: str