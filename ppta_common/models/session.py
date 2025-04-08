from mongoengine import StringField, BooleanField, ListField, IntField, ReferenceField, DateTimeField
from .base_document import BaseDocument
from .available_period import AvailablePeriod

class Session(BaseDocument):
    coaching = ReferenceField('Coaching', required=False)
    is_client_absent = BooleanField(default=False)
    is_coach_absent = BooleanField(default=False)
    meeting_link = StringField(required=True)
    event_id = StringField(required=True)
    notification_before = ListField(IntField(), required=False)
    is_confirmed = BooleanField(default=False)
    date = IntField(required=True)
    start_time = IntField(required=True)
    end_time = IntField(required=True)
    timezone = StringField(required=True)
    is_cancelled = BooleanField(default=False)
    additional_participants_emails = ListField(StringField(), required=False)
    period = ReferenceField('AvailablePeriod', required=True)
    