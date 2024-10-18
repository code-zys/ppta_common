import datetime
from mongoengine import  StringField, ReferenceField, ListField, IntField, DictField, EnumField
from .base_document import BaseDocument
from .user import User
from .company import Company
from ..utils.enums import EnumRole
from enum import Enum


class NotificationType(str, Enum):
    COMPANY = 'COMPANY'
    MEMBER = 'MEMBER'
    GENERAL = 'GENERAL'

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
    from_user = ReferenceField(User, required=True)
    to_user = ReferenceField(User, required=False)
    to_company = ReferenceField(Company, required=False)
    recipient_roles = ListField(StringField(choices=[e.value for e in EnumRole], required=True), default=[])

    def __str__(self):
        return f"Notification:{self.room}, {self.message}"