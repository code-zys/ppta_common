import datetime
from mongoengine import EmbeddedDocument, StringField, DateTimeField

class GoogleMeet(EmbeddedDocument):
    name = StringField(required=True)
    candidate_email = StringField(required=True)
    final_client_email = StringField(required=True)
    recruter_email = StringField(required=False)
    interview_date = DateTimeField(required=True)
    start_time: datetime
    end_time: datetime
    