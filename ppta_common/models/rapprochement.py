from mongoengine import StringField, ReferenceField, EmbeddedDocumentField
from .base_document import BaseDocument
from .bank_transaction import BankTransaction
from .company import Company
from .run_invoice_content import RunInvoiceContent
from ..enums.rapprochement_type_enum import EnumRapprochementType
from .printed_invoice import PrintedInvoice


class Rapprochement(BaseDocument):
    printed_invoice = ReferenceField(PrintedInvoice, required=False)
    run_invoice_content = ReferenceField(RunInvoiceContent, required=False)
    transaction = ReferenceField(BankTransaction, required=True)
    company_id = ReferenceField(Company, required=True, default=None)
    rapprochement_type  = StringField(choices=[e.value for e in EnumRapprochementType], required=True, default=EnumRapprochementType.DEBIT.value)
    meta = {
        'collection': 'rapprochement',
        "strict": False
    }