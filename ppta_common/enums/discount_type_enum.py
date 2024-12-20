from enum import Enum


class EnumDiscountType(str,Enum):
    PERCENTAGE = "PERCENTAGE"
    AMOUNT = "AMOUNT"
    