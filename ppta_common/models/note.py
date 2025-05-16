from mongoengine import StringField, ReferenceField, IntField
from .base_document import BaseDocument
from .session import Session
from ..enums.session_note_reason import SessionNoteReason

class Note(BaseDocument):
    value = IntField(required=True)
    comment = StringField(required=False)
    client = StringField(required=False) #TODO: To be removed
    coach_id = StringField(required=True)
    coaching_id = StringField(required=True)
    session = ReferenceField(Session, required=True)