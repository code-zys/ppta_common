
from mongoengine import EmbeddedDocument, StringField, IntField, FloatField

class TransactionReconciliation(EmbeddedDocument):
    invoice_id = StringField(required=True)
    invoice_type = StringField(required=True) # PrintedInvoice or RunInvoiceContent
    percentage = FloatField(required=True)
    date = IntField(required=True)
    file_path = StringField(required=True)

    meta = {
        "strict": False,
    }