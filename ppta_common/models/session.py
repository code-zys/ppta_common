from mongoengine import StringField, BooleanField, ListField, IntField, ReferenceField, DateTimeField
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
    start_date = DateTimeField(required=True)
    end_date = DateTimeField(required=True)
    timezone = StringField(required=True)
    is_cancelled = BooleanField(default=False)
    additional_participants_emails = ListField(StringField(), required=False)
    period_id = ReferenceField('AvailablePeriod', required=True)
    