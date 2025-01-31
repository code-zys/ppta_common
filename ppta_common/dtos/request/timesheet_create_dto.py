
from pydantic import BaseModel
from ...enums.timesheet_type_enum import TimesheetType

class TimesheetCreateDTO(BaseModel):
    month: str
    year: int
    mission: str
    type: TimesheetType