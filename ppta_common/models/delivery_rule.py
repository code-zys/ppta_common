from mongoengine import StringField, BooleanField, EnumField, EmbeddedDocument, DateTimeField
from utils.enums import DeliveryRuleModeEnum
from datetime import datetime

class DeliveryRule(EmbeddedDocument):
    id = StringField()
    title = StringField()
    receiver = StringField()
    mode = EnumField(DeliveryRuleModeEnum)
    receiver_mail = StringField()
    api = StringField()
    validate_before = BooleanField()
    invoice_id = StringField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=None)
   
