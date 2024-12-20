from enum import Enum


class InvoiceCategoryType(str,Enum):
    DEVIS = "DEVIS"
    INVOICE = "INVOICE"