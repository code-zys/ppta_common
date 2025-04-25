from mongoengine import StringField, ReferenceField, IntField
from .base_document import BaseDocument
from .session import Session
from ..enums.session_note_reason import SessionNoteReason

class Note(BaseDocument):
    value = IntField(required=True)
    comment = StringField(required=False)
    reason  = StringField(choices=[e.value for e in SessionNoteReason], required=False, default=None)
    client = StringField(required=True)
    coach_id = StringField(required=True)
    coaching_id = StringField(required=True)
    session = ReferenceField(Session, required=True)