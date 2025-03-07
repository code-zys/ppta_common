from pydantic import BaseModel, HttpUrl

class ApplicationCreateDto(BaseModel):
    message: str
    cv: HttpUrl
    mission_id: str
    applied_for_consultant_id: str