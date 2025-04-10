from enum import Enum

class EnumWithdrawRequestStatus(Enum):
    ACCEPTED = "ACCEPTED"
    REFUSED = "REFUSED"
    PENDING = "PENDING"