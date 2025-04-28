from mongoengine import StringField, BooleanField, ListField, IntField, ReferenceField, FloatField
from .base_document import BaseDocument
from .available_period import AvailablePeriod
from ..enums.session_status_enum import EnumSessionStatus

class Session(BaseDocument):
    coaching = ReferenceField('Coaching', required=True)
    is_client_absent = BooleanField(default=False)
    is_coach_absent = BooleanField(default=False)
    payment_id = StringField(required=False)
    meeting_link = StringField(required=False)
    event_id = StringField(required=False)
    notification_before = ListField(IntField(), required=False)
    additional_participants_emails = ListField(StringField(), required=False)
    period = ReferenceField('AvailablePeriod', required=True)
    iyvo_income = FloatField(required=False)
    coach_income = FloatField(required=False)
    status = StringField(choices=[e.value for e in EnumSessionStatus], required=True, default=EnumSessionStatus.DRAFT)
    is_payment_transfered_to_coach = BooleanField(default=False)
    payment_transfered_to_coach_at = IntField(default=False)
    payment_intent=StringField(required=False)
    