from mongoengine import StringField, BooleanField, ListField, IntField, ReferenceField
from .time_range import TimeRange
from .base_document import BaseDocument

class Session(BaseDocument):
    time_range = ReferenceField(TimeRange, required=True)
    is_client_absent = BooleanField(default=False)
    is_coach_absent = BooleanField(default=False)
    meeting_link = StringField(required=True)
    event_id = StringField(required=True)
    notification_before = ListField(IntField(), required=False)
    is_confirmed = BooleanField(default=False)