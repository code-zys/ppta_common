from mongoengine import StringField, BooleanField, EnumField, EmbeddedDocument, IntField
from utils.enums import ExportType, EnumConnectionStatus

class CollectRule(EmbeddedDocument):
    id = StringField()
    subject = StringField()
    title = StringField()
    collected_from = StringField()
    to = StringField()
    has_attachment = BooleanField()
    has_word = BooleanField()
    before = StringField()
    after = StringField()
    contain = StringField()
    search = StringField()
    connection_id = StringField()
    export = EnumField(ExportType)
    invoice_id = StringField()
    created_at = IntField(required=True)
    updated_at = IntField(default=None)
    last_connection_date = IntField(default=None)
    last_connection_status = StringField(choices=[e.value for e in EnumConnectionStatus], default=EnumConnectionStatus.NOT_TESTED)

