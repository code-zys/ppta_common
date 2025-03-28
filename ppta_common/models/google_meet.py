from mongoengine import EmbeddedDocument, StringField, DateTimeField

class GoogleMeet(EmbeddedDocument):
    candidate_email = StringField(required=True)
    final_client_email = StringField(required=True)
    recruter_email = StringField(required=False)
    interview_date = DateTimeField(required=True)
    