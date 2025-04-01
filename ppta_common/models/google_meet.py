import datetime
from mongoengine import EmbeddedDocument, StringField, DateTimeField, IntField, ListField

class GoogleMeet(EmbeddedDocument):
    name = StringField(required=True)
    description = StringField(required=True)
    link = StringField(required=True)
    candidate_email = StringField(required=True)
    interview_date = StringField(required=True)
    start_time = StringField(required=True)
    end_time = StringField(required=True)
    notification_before = ListField(IntField(), required=False)
    additional_participants_email = ListField(StringField(), required=False)
    