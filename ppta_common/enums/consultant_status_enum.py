from enum import Enum
class EnumConsultantStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    REFUSED = "REFUSED"
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"