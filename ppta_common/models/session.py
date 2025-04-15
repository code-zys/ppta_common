from mongoengine import StringField, BooleanField, ListField, IntField, ReferenceField, FloatField
from .base_document import BaseDocument
from .available_period import AvailablePeriod
from ..enums.session_status_enum import EnumSessionStatus

class Session(BaseDocument):
    coaching = ReferenceField('Coaching', required=True)
    is_client_absent = BooleanField(default=False)
    is_coach_absent = BooleanField(default=False)
    meeting_link = StringField(required=False)
    event_id = StringField(required=False)
    notification_before = ListField(IntField(), required=False)
    is_confirmed = BooleanField(default=False)
    additional_participants_emails = ListField(StringField(), required=False)
    period = ReferenceField('AvailablePeriod', required=True)
    iyvo_income = FloatField(required=False)
    coach_income = FloatField(required=False)
    status = StringField(choices=[e.value for e in EnumSessionStatus], required=False)
    