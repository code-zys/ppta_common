
from pydantic import BaseModel
from ...enums.timesheet_type_enum import TimesheetType

class TimesheetCreateDTO(BaseModel):
    month: str
    year: int
    mission: str
    #TODO: make use of user_type in member, type should be removed. Make use of member to whom the mission is assigned