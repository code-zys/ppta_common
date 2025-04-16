from enum import Enum


class EnumSessionStatus(Enum):
    COMPLETED = "COMPLETED"
    DRAFT = "DRAFT"
    CANCELLED = "CANCELLED"
    PAID_BUT_NOT_COMPLETED = "PAID_BUT_NOT_COMPLETED"