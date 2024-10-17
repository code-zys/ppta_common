import datetime
from mongoengine import  StringField, ReferenceField, ListField, IntField, DictField, EnumField
from .base_document import BaseDocument
from .user import User
from .company import Company
from ..utils.enums import EnumRole


class Notification(BaseDocument):
    """
    Notification
    """
    room = StringField(required=True)
    message = StringField(required=True)
    notification_type = StringField(default="general")
    object = DictField()
    status = EnumField(choices=["unread", "read"], default="unread")
    to_user = ReferenceField(User, required=False)
    to_company = ReferenceField(Company)
    recipient_roles = ListField(StringField(choices=[e.value for e in EnumRole], required=True), default=[])
    created_at = IntField(default=None)

    def __str__(self):
        return f"Notification:{self.room}, {self.message}"