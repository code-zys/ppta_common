from mongoengine import StringField, FloatField, ReferenceField, IntField, EmbeddedDocumentField, ListField
from ..models.card import Card
from ..models.coach import Coach
from ..enums.card_type_enum import EnumCardType
from .base_document import BaseDocument
from ..enums.withdraw_request_status_enum import EnumWithdrawRequestStatus

class Withdrawal(BaseDocument):
    amount_withdrawn = FloatField(required=False)
    type = StringField(choices=[e.value for e in EnumCardType], required=False)
    coach = ReferenceField(Coach, required=False)
    receipt = StringField(required=False)
    card = EmbeddedDocumentField(
        Card, description="The card of the withdrawal", required=False
    )
    date = IntField(required=False, description="The date of the withdrawal")
    status = StringField(choices=[e.value for e in EnumWithdrawRequestStatus], required=True)
    accepted_at = IntField(required=False, description="The date of the withdrawal acceptance")
    refused_at = IntField(required=False, description="The date of the withdrawal refused")
    financial_lines = ListField(StringField, required=True, description="The The list of finacial line to be use on this widrwal")