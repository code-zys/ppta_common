from mongoengine import StringField, EmbeddedDocumentField, BooleanField, ReferenceField, ListField
from .base_document import BaseDocument
from .session import Session
from .coach import Coach

class Coaching(BaseDocument):
    coach_id = ReferenceField(Coach, required=True)
    client = StringField(required=True)
    payment_id = StringField(required=True)
    date = StringField(required=True)
    meeting_link = StringField(required=False)
    description = StringField(required=False)
    name = StringField(required=True)
    sessions = ListField(EmbeddedDocumentField(Session), required=True)
    user = StringField(required=True)
    is_confirmed = BooleanField(default=False)