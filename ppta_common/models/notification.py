import datetime
from mongoengine import  StringField, ReferenceField, ListField, IntField, DictField, EnumField, EmbeddedDocumentField
from .user_metadata import UserMetadata
from .base_document import BaseDocument
from .user import User
from .company import Company
from ..utils.enums import EnumRole
from enum import Enum


class NotificationType(str, Enum):
    PUNCTUAL_COLLECTION_STARTED = 'PUNCTUAL_COLLECTION_STARTED'
    MONTHLY_COLLECTION_STARTED = 'MONTHLY_COLLECTION_STARTED'
    PUNCTUAL_COLLECTION_ENDED = 'PUNCTUAL_COLLECTION_ENDED'
    MONTHLY_COLLECTION_ENDED = 'MONTHLY_COLLECTION_ENDED'
    PUNCTUAL_COLLECTION_FAILED = 'PUNCTUAL_COLLECTION_FAILED'
    MONTHLY_COLLECTION_FAILED = 'MONTHLY_COLLECTION_FAILED'
    COMPANY_INVITATION_SENT = 'COMPANY_INVITATION_SENT'
    ACCOUNTANT_INVITATION_SENT = 'ACCOUNTANT_INVITATION_SENT'
    COMPANY_INVITATION_ACCEPTED = 'COMPANY_INVITATION_ACCEPTED'
    ACCOUNTANT_INVITATION_ACCEPTED = 'ACCOUNTANT_INVITATION_ACCEPTED'
    DOCUMENT_SHARED_WITH_ACCOUNTANT = 'DOCUMENT_SHARED_WITH_ACCOUNTANT'
    PDF_CONVERSION_SUCCESS = 'PDF_CONVERSION_SUCCESS'
    PDF_CONVERSION_FAILED = 'PDF_CONVERSION_FAILED'
    FILE_OWNER_CHANGED = 'FILE_OWNER_CHANGED'
    PAYMENT_SUCCESS = 'PAYMENT_SUCCESS'
    PAYMENT_FAILED = 'PAYMENT_FAILED'
    SUBSCRIBE_TO_PLAN = 'SUBSCRIBE_TO_PLAN'
    APPLICATION_SENT = 'APPLICATION_SENT'
    NEW_APPLICATION_RECEIVED = 'NEW_APPLICATION_RECEIVED'
    EXTERNAL_CONSULTANT_INVITATION_SENT = 'EXTERNAL_CONSULTANT_INVITATION_SENT'
    INTERNAL_CONSULTANT_INVITATION_SENT = 'INTERNAL_CONSULTANT_INVITATION_SENT'

class NotificationStatus(str, Enum):
    READ = 'READ'
    UNREAD = 'UNREAD'

class Notification(BaseDocument):
    """
    Notification
    """
    room = StringField(required=True)
    message = StringField(required=True)
    notification_type = StringField(choices=[e.value for e in NotificationType], required=True)
    data = DictField()
    status = StringField(choices=[e.value for e in NotificationStatus], required=True, default=NotificationStatus.UNREAD.value)
    from_user = ReferenceField(User, required=False)
    to_user = ReferenceField(User, required=False)
    to_company = ReferenceField(Company, required=False)
    recipient_roles = ListField(StringField(choices=[e.value for e in EnumRole], required=True), default=[])
    read_at = IntField(default=None)
    read_by = EmbeddedDocumentField(UserMetadata)

    def __str__(self):
        return f"Notification:{self.room}, {self.message}"