from mongoengine import EmbeddedDocument, StringField, BooleanField, EmbeddedDocumentField
from .time_range import TimeRange

class Session(EmbeddedDocument):
    time_range = EmbeddedDocumentField(TimeRange, required=True)
    is_client_absent = BooleanField(default=False)
    is_coach_absent = BooleanField(default=False)
    meeting_link = StringField(required=True)