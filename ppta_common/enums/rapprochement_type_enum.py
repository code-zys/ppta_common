from enum import Enum


class EnumRapprochementType(str, Enum):
    DEBIT = 'DEBIT'
    CREDIT = 'CREDIT'