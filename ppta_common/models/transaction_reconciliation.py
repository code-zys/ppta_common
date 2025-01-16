from mongoengine import EmbeddedDocument, StringField, IntField, FloatField
from ..enums.invoice_type import EnumInvoiceType

class TransactionReconciliation(EmbeddedDocument):
    invoice_id = StringField(required=True)
    invoice_type  = StringField(choices=[e.value for e in EnumInvoiceType], required=True, default=EnumInvoiceType.NONE.value)
    percentage = FloatField(required=True)
    date = IntField(required=True)
    file_path = StringField(required=True)
    file_name = StringField(required=True)

    meta = {
        "strict": False,
    }