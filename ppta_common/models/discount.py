from mongoengine import StringField, FloatField, EmbeddedDocument
from ..enums.discount_type_enum import EnumDiscountType

class Discount(EmbeddedDocument):
    val = FloatField(required=True, default=0.0)
    type = StringField(choices=[e.value for e in EnumDiscountType], required=True, default=EnumDiscountType.AMOUNT.value)