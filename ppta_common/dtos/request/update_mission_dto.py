from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class MissionUpdateDto(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    application_id: Optional[str] = None