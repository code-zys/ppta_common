from mongoengine import StringField, IntField

from .base_document import BaseDocument
from ..utils.enums import EnumConnectionStatus

class MailConnection(BaseDocument):
    type = StringField(required=True)
    title = StringField(required=True)
    last_connection_date = IntField(default=None)
    last_connection_status = StringField(choices=[e.value for e in EnumConnectionStatus], default=EnumConnectionStatus.NOT_TESTED)

    meta = {
        'abstract': True,  # This makes the base class abstract
    }