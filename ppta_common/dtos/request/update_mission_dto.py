from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from ...enums.mission_status_enum import MissionStatus

class MissionUpdateDto(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    # application_id: Optional[str] = None
    consultant_id: Optional[str] = None
    status: Optional[MissionStatus] = None