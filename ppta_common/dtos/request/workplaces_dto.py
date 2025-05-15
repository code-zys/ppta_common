from typing import List, Optional

from pydantic import BaseModel


class SkillDto(BaseModel):
    code: str
    name: str
    percent: float = 0
    link_to_video: str = None
    description: str = None


class WorkPlaceCreationDto(BaseModel):
    client: str
    verified: bool = False
    skills: Optional[List[SkillDto]] = []
    position: str
    description: str
    start_date: Optional[int] = None
    end_date: Optional[int] = None
