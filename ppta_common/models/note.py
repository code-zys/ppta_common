from mongoengine import StringField, ReferenceField, IntField
from .base_document import BaseDocument
from .coaching import Coaching
class Note(BaseDocument):
    name = StringField(required=True)
    value = IntField(required=True)
    comment = StringField(required=False)
    client = StringField(required=True)
    coach_id = StringField(required=True)
    coaching_id = ReferenceField(Coaching, required=True)