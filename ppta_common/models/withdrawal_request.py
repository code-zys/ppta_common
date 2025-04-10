from mongoengine import StringField, FloatField, ReferenceField, IntField
from .coach import Coach
from ..enums.withdraw_request_status_enum import EnumWithdrawRequestStatus
from .base_document import BaseDocument

class WithdrawalRequest(BaseDocument):
    amount = FloatField(required=False)
    status = StringField(choices=[e.value for e in EnumWithdrawRequestStatus], required=True)
    coach = ReferenceField(Coach, required=False)
    date = IntField(required=False, description="The date of the withdrawal")
    accepted_at = IntField(required=False, description="The date of the withdrawal acceptance")
    refused_at = IntField(required=False, description="The date of the withdrawal refused")