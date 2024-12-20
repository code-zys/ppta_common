from mongoengine import EmbeddedDocument, FloatField

class Totals(EmbeddedDocument):
    subtotal_ht = FloatField(required=True, default=0.0)
    vat_total = FloatField(required=True, default=0.0)
    total_ttc = FloatField(required=True, default=0.0)