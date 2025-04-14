from enum import Enum

class EnumAvailablePeriodStatus(str, Enum):
    ON_GOING = "ON_GOING"
    OCCUPIED = "OCCUPIED"
    NOT_OCCUPIED = "NOT_OCCUPIED"