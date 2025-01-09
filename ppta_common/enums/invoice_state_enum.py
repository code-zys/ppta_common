from enum import Enum

class EnumInvoiceState(str, Enum):
    INITIAL = 'INITIAL'
    GENERATED = 'GENERATED'
    APROUVED  = 'APROUVED'