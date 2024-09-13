from enum import Enum


class InvoiceClassType(str, Enum):
    STANDARD = 'STANDARD'
    SYSTEM = 'SYSTEM'