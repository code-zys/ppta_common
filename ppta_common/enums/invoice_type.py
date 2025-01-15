from enum import Enum

class EnumInvoiceType(str, Enum):
    RUN_INVOICE_CONTENT = 'RUN_INVOICE_CONTENT'
    PRINTED_INVOICE = 'PRINTED_INVOICE'
    NONE = 'NONE'