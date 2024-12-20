from mongoengine import StringField, FloatField, IntField, EmbeddedDocument
from ..enums.discount_type_enum import EnumDiscountType
from ..enums.mesure_unit_enum import EnumMesureUnit

class QuoteItem(EmbeddedDocument):
    label = StringField(required=True, default="")
    description = StringField(required=True, default="")
    unit_price_ht = FloatField(required=True, default=0.0)
    quantity = IntField(required=True, default=1)
    tax_rate = FloatField(required=True, default=0.0)
    discountValue = FloatField(required=False, default=0.0)
    discountType = StringField(choices=[e.value for e in EnumDiscountType], required=False)
    unit = StringField(choises=[e.value for e in EnumMesureUnit], required=False)