from mongoengine import EmbeddedDocument, StringField, IntField
from ..enums.payment_condition_unit_enum import EnumPaymentConditionUnit

class PaymentCondition(EmbeddedDocument):
    unit= StringField(choices=[e.value for e in EnumPaymentConditionUnit], required=True) 
    val= IntField(required=True)