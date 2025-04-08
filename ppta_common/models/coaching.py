from mongoengine import StringField, BooleanField, ReferenceField, ListField, DateField
from .base_document import BaseDocument
from .session import Session
from .coach import Coach

class Coaching(BaseDocument):
    coach_id = ReferenceField(Coach, required=True)
    client = StringField(required=True)
    payment_id = StringField(required=True)
    description = StringField(required=False)
    name = StringField(required=True)
    sessions = ListField(ReferenceField(Session), required=True)
    user = StringField(required=True)
    is_confirmed = BooleanField(default=False)
    is_cancelled = BooleanField(default=False)