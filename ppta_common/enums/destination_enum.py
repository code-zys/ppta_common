from enum import Enum

class EnumDestinationStatus(str, Enum):
    COACH = "COACH"
    APP = "APP"
    USER = "USER"