from enum import Enum


class EnumInvoiceTemplateFormatType(str, Enum):
    A4 = "A4"
    LETTER = "Letter"
    A5 = "A5"
    CUSTOM = "Custom"