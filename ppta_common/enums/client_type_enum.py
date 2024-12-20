from enum import Enum


class EnumClientType(str,Enum):
    COMPANY = "COMPANY"
    INDIVIDUAL = "INDIVIDUAL"