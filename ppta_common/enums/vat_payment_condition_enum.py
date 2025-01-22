from enum import Enum

class EnumVatPaymentCondition(str,Enum):
    ON_RECEIPTS = "ON_RECEIPTS"
    ON_DEBITS = "ON_DEBITS"
    EXEMPTION = "EXEMPTION"