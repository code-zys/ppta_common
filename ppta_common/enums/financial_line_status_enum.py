from enum import Enum

class EnumFinancialLineStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    TO_BE_PAID = "TO_BE_PAID"
    IN_WITHDRAWN= "IN_WITHDRAWN"
    CANCELLED = "CANCELLED"
    PAID = "PAID"
    REQUIRES_ACTION = "REQUIRES_ACTION"