from enum import Enum

class TimeSheetLevel(Enum):
    CONSULTANT = "CONSULTANT"
    SUPERVISOR = "SUPERVISOR"
    CLIENT = "CLIENT"
    VALIDATED = "VALIDATED"