from mongoengine import StringField,IntField, ReferenceField, FloatField, DictField
from .base_document import BaseDocument
from ppta_common.models.session import Session
from ppta_common.models.coaching import Coaching
from ppta_common.models.coach import Coach
from ppta_common.enums.financial_line_type_enum import EnumFinancialLineType
from ppta_common.enums.financial_line_status_enum import EnumFinancialLineStatus
from ppta_common.enums.destination_enum import EnumDestinationStatus

class FinancialLine(BaseDocument):
    session = ReferenceField(Session, required=True)
    date = IntField(required=False)
    transaction_id = StringField(required=False)
    client = StringField(required=False)
    amount = FloatField(required=False)
    start_date  = IntField(required=True)
    end_date  = IntField(required=True)
    coaching = ReferenceField(Coaching, required=True)
    coach = ReferenceField(Coach, required=True)
    type = StringField(choices=[e.value for e in EnumFinancialLineType], required=True)
    paid_at = IntField(default=False)
    status = StringField(choices=[e.value for e in EnumFinancialLineStatus], required=True)
    cancelled_at = IntField(required=False)
    destination = StringField(choices=[e.value for e in EnumDestinationStatus], required=True)
    metadata = DictField(required=False)