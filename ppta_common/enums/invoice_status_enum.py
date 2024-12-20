from enum import Enum


class EnumInvoiceStatus(str, Enum):
    PAID = 'PAID'
    UNPAID = 'UNPAID'