import datetime
from mongoengine import EmbeddedDocument, StringField, DateTimeField, IntField

class GoogleMeet(EmbeddedDocument):
    name = StringField(required=True)
    description = StringField(required=True)
    link = StringField(required=True)
    candidate_email = StringField(required=True)
    recruter_email = StringField(required=False)
    interview_date = DateTimeField(required=True)
    start_time: datetime
    end_time: datetime
    notification_before = IntField(required=False)
    