from mongoengine import StringField, BooleanField, ListField, IntField, ReferenceField, FloatField, EmbeddedDocumentField
from .base_document import BaseDocument
from .available_period import AvailablePeriod
from ..enums.session_status_enum import EnumSessionStatus
from .session_feedback import SessionFeedback

class Session(BaseDocument):
    coaching = ReferenceField('Coaching', required=True)
    cancel_by_coach = BooleanField(default=False)
    cancel_by_client = BooleanField(default=False)
    payment_id = StringField(required=False)
    meeting_link = StringField(required=False)
    event_id = StringField(required=False)
    notification_before = ListField(IntField(), required=False)
    additional_participants_emails = ListField(StringField(), required=False)
    period = ReferenceField('AvailablePeriod', required=True)
    status = StringField(choices=[e.value for e in EnumSessionStatus], required=True, default=EnumSessionStatus.DRAFT)
    payment_transfered_to_coach_at = IntField(default=False)
    payment_intent=StringField(required=False)
    cancelled_at = IntField(required=False)
    total_ht = FloatField(required=False)
    total_ttc = FloatField(required=False)
    amount_to_transfer = FloatField(
        required=False,
        description="In the case de user cancel or the coach cancel the amount will not be the coach_income",
    )
    note_expired_time = IntField(required=False)
    session_feedback = EmbeddedDocumentField(SessionFeedback, required=False)
    