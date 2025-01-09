from mongoengine import EmbeddedDocument, FloatField

class Totals(EmbeddedDocument):
    vat_value = FloatField(required=True, default=0.0)
    vat_percent = FloatField(required=True, default=0.0)
    ttc = FloatField(required=True, default=0.0)
    ht = FloatField(required=True, default=0.0)