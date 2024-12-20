from mongoengine import StringField, FloatField, EmbeddedDocument
from ..enums.discount_type_enum import EnumDiscountType
from ..enums.mesure_unit_enum import EnumMesureUnit

class InvoiceItem(EmbeddedDocument):
    description = StringField(required=True, default="")
    label = StringField(required=True, default="")
    unit_price_ht = FloatField(required=True, default=0.0)
    tax_rate = FloatField(required=False, default=0.0)
    discountValue = FloatField(required=False, default=0.0)
    discountType = StringField(choices=[e.value for e in EnumDiscountType], required=False)
    unit = StringField(choices=[e.value for e in EnumMesureUnit], required=False)
    quantity = FloatField(required=False, default=None)