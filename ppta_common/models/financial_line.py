from mongoengine import StringField,IntField, ReferenceField, BooleanField, FloatField
from .base_document import BaseDocument
from ppta_common.models.session import Session
from ppta_common.models.coaching import Coaching
from ppta_common.models.coach import Coach
from ppta_common.enums.financial_line_type_enum import EnumFinancialLineType, EnumRefundReason
from ppta_common.enums.financial_line_status_enum import EnumFinancialLineStatus
from ppta_common.enums.destination_enum import EnumDestinationStatus

class FinancialLine(BaseDocument):
    session = ReferenceField(Session, required=True)
    date = IntField(required=False) #TODO: To be removed
    transaction_id = StringField(required=False) #TODO: To be removed 
    client = StringField(required=False) #TODO: To be removed 
    amount = IntField(required=False) #TODO: To be removed 
    start_date = IntField(required=False) #TODO: To be removed 
    end_date = IntField(required=False) #TODO: To be removed 
    coaching = ReferenceField(Coaching, required=False) #TODO: To be removed
    coach = ReferenceField(Coach, required=False) #TODO: To be removed
    coaching_id = StringField(required=False)
    coach_id = StringField(required=False)
    type = StringField(choices=[e.value for e in EnumFinancialLineType], required=True)
    paid_at = IntField(default=False)
    status = StringField(choices=[e.value for e in EnumFinancialLineStatus], required=True)
    cancelled_at = IntField(required=False)
    invoice_link = StringField(required=False) 
    destination = StringField(choices=[e.value for e in EnumDestinationStatus], required=True)
    refund_reason = StringField(choices=[e.value for e in EnumRefundReason], required=False)
    is_full_refund = BooleanField(required=False) # Used to distinguish between a full refund and a partial refund
    total_ht = FloatField(required=False)
    total_ttc = FloatField(required=False)
    is_transferable = BooleanField(default=True)
    transfer_id = StringField(required=False)
    refund_id = StringField(required=False)