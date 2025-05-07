from mongoengine import EmbeddedDocument, BooleanField, StringField, IntField
from ..enums.session_note_reason import SessionNoteReason

class SessionFeedback(EmbeddedDocument):
    is_session_good = BooleanField(default=True)
    should_refund = BooleanField(default=False, required=False)
    reason = StringField(choices=[e.value for e in SessionNoteReason], required=False, default=None)
    description = StringField(required=False)
    feedback_at = IntField(required=False)
