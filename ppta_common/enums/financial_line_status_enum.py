from enum import Enum

class EnumFinancialLineStatus(str, Enum):
    PAID = "PAID"
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    TO_BE_PAID = "TO_BE_PAID"