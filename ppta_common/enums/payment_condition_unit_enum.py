from enum import Enum

class EnumPaymentConditionUnit(str,Enum):
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"
    HOUR = "HOUR"