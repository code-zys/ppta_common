from enum import Enum


class EnumSessionStatus(Enum):
    COMPLETED = "COMPLETED"
    DRAFT = "DRAFT"
    CANCELLED = "CANCELLED"
    CONFIRMED = "CONFIRMED"
    REQUIRED_ACTION = "REQUIRED_ACTION"