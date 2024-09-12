from enum import Enum


class InvoiceClassType(str, Enum):
    #INVOICE = 'INVOICE'
    #NOTE_DE_FRAIS = 'NOTE_DE_FRAIS'

    STANDARD = 'STANDARD'
    SYSTEM = 'SYSTEM'