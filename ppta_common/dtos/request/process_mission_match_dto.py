from ...enums.mission_match_type_enum import MissionMatchType
from typing import Optional

class ProcessMissionMatchDto:
    def __init__(
        self,
        company_id: str,
        type: MissionMatchType,
        member_id: Optional[str] = None,
        mission_id: Optional[str] = None,
    ):
        self.company_id = company_id
        self.member_id = member_id
        self.mission_id = mission_id
        self.type = type
    def __str__(self):
        return f"ProcessMissionMatchDto(company_id: {self.company_id}, member_id: {self.member_id}, mission_id: {self.mission_id}, type: {self.type})"