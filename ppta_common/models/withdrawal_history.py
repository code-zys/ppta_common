from mongoengine import StringField, FloatField
from ..enums.card_type_enum import EnumCardType
from .base_document import BaseDocument

class WithdrawalHistory(BaseDocument):
    amount_withdrawn = FloatField(required=False)
    type = StringField(choices=[e.value for e in EnumCardType], required=True)
    coach = StringField(required=False)
    receipt = StringField(required=False)