from enum import Enum


class EnumInvoiceTemplateType(str, Enum):
    STANDARD = "Standard"  # Modèle générique pour factures
    PROFORMA = "Proforma"  # Facture proforma
    CREDIT_NOTE = "Credit Note"  # Note de crédit
    DELIVERY_NOTE = "Delivery Note"  # Bon de livraison
    CUSTOM = "Custom"  # Modèle personnalisé