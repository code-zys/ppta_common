from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MissionCreateDto(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    application_id: str