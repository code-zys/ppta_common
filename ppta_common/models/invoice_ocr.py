from mongoengine import EmbeddedDocument
from mongoengine.fields import (
    StringField, DateTimeField, FloatField, DictField, EmbeddedDocumentField)
from iso4217 import Currency
from .total import Totals

class InvoiceOCR(EmbeddedDocument):
    invoice_id = StringField(required=True)
    currency = StringField(choices=[c.value for c in Currency], required=True)
    total = EmbeddedDocumentField(Totals, required=True)
    invoice_date = DateTimeField(required=True)
    sender_name = StringField(required=True)
    sender_address = StringField(required=True)
    meta = {
        "strict": False
    }
   