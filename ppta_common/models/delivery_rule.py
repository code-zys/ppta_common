from mongoengine import StringField, BooleanField, EnumField, EmbeddedDocument, IntField
from ..utils.enums import DeliveryRuleModeEnum
from datetime import datetime

class DeliveryRule(EmbeddedDocument):
    id = StringField()
    title = StringField()
    receiver = StringField()
    mode = StringField(choices=[e.value for e in DeliveryRuleModeEnum])
    receiver_mail = StringField()
    api = StringField()
    validate_before = BooleanField()
    invoice_id = StringField()
    created_at = IntField(default=datetime.now)
    updated_at = IntField(default=None)
   
