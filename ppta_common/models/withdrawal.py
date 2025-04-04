from mongoengine import StringField, FloatField, ReferenceField, IntField, EmbeddedDocumentField
from ..models.card import Card
from ..models.coach import Coach
from ..enums.card_type_enum import EnumCardType
from .base_document import BaseDocument

class Withdrawal(BaseDocument):
    amount_withdrawn = FloatField(required=False)
    type = StringField(choices=[e.value for e in EnumCardType], required=True)
    coach = ReferenceField(Coach, required=False)
    receipt = StringField(required=False)
    card = EmbeddedDocumentField(
        Card, description="The card of the withdrawal", required=False
    )
    date = IntField(required=False, description="The date of the withdrawal")