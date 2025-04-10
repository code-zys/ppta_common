from mongoengine import StringField, BooleanField, ListField, IntField, ReferenceField, FloatField
from .base_document import BaseDocument
from .available_period import AvailablePeriod

class Session(BaseDocument):
    coaching = ReferenceField('Coaching', required=True)
    is_client_absent = BooleanField(default=False)
    is_coach_absent = BooleanField(default=False)
    meeting_link = StringField(required=True)
    event_id = StringField(required=True)
    notification_before = ListField(IntField(), required=False)
    is_confirmed = BooleanField(default=False)
    is_cancelled = BooleanField(default=False)
    additional_participants_emails = ListField(StringField(), required=False)
    period = ReferenceField('AvailablePeriod', required=True)
    iyvo_income = FloatField(required=False)
    coach_income = FloatField(required=False)
    