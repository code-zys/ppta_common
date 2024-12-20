from enum import Enum


class EnumPaymentCondition(str,Enum):
    ON_RECEIPT = "ON_RECEIPT"
    IN_15_DAYS = "IN_15_DAYS"
    IN_30_DAYS = "IN_30_DAYS"
    CUSTOM = "CUSTOM"