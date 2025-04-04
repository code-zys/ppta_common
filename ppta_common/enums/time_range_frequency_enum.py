from enum import Enum

class FrequencyEnum(str, Enum):
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    PONTUAL = "PONTUAL"