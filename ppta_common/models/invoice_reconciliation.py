from mongoengine import StringField, IntField, FloatField, EmbeddedDocument

class InvoiceReconciliation(EmbeddedDocument):
    transaction_id = StringField(required=True)
    percentage = FloatField(required=True)
    date = IntField(required=True)

    meta = {
        "strict": False,
    }