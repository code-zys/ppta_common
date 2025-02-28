from mongoengine import EmbeddedDocument
from mongoengine.fields import (
    StringField, DateTimeField, FloatField, DictField, EmbeddedDocumentField)
from iso4217 import Currency
from .total import Totals

class InvoiceOCR(EmbeddedDocument):
    invoice_id = StringField(required=False)
    currency = StringField(choices=[c.value for c in Currency], required=False)
    total = EmbeddedDocumentField(Totals, required=False)
    invoice_date = DateTimeField(required=False)
    sender_name = StringField(required=False)
    sender_address = StringField(required=False)
    pricing = DictField(field=EmbeddedDocumentField(Totals), required=False, default={})

    meta = {
        'strict': False
    }
