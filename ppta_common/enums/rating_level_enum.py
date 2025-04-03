from enum import Enum

class EnumRatingLevel(str, Enum):
    VERY_SATISFIED = "VERY_SATISFIED"
    SATISFIED = "SATISFIED"
    NEUTRAL = "NEUTRAL"
    UNSATISFIED = "UNSATISFIED"