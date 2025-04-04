from mongoengine import EmbeddedDocument, StringField, DateTimeField, IntField, ListField

class GoogleMeet(EmbeddedDocument):
    name = StringField(required=True)
    description = StringField(required=True)
    link = StringField(required=True)
    candidate_email = StringField(required=True)
    interview_date = DateTimeField(required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    notification_before = ListField(IntField(), required=False)
    additional_participants_email = ListField(StringField(), required=False)
    