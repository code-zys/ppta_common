from enum import Enum


class EnumMesureUnit(str,Enum):
    UNIT = "UNIT"
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"
    MINUTE = "MINUTE"