from mongoengine import EmbeddedDocument
from mongoengine.fields import (
    StringField, DateTimeField, FloatField)

class InvoiceOCR(EmbeddedDocument):
    invoice_id = StringField(required=True)
    total_amount = FloatField(required=True)
    currency = StringField(required=True)
    tva_number = StringField()  # Optional
    tva_value = StringField()  # Optional
    invoice_date = DateTimeField(required=True)
    sender_name = StringField(required=True)
    sender_address = StringField(required=True)