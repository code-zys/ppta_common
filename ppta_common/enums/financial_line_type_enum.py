from enum import Enum

class EnumRefundReason(str, Enum):
    CANCELLED = "CANCELLED"
    ATTENDEES = "ATTENDEES"
    LITIGATION = "LITIGATION"

class EnumFinancialLineType(str, Enum):
    COACHING = "COACHING"
    CANCELLED = "CANCELLED" #TODO: To be removed
    REFUND = "REFUND"