from mongoengine import StringField, ListField, BooleanField, \
    EmbeddedDocument, DateTimeField, EnumField
from utils.enums import FrequencyEnum, ExportType


class RunCollectRule(EmbeddedDocument):
    """
    RunCollectRule document
    """
    subject = StringField()
    has_attachment = BooleanField()
    export = EnumField(ExportType, default=ExportType.BODY)
    mail_found_ids = ListField(StringField())
    before = DateTimeField()
    after = DateTimeField()
    invoice_id = StringField()
    connection_id = StringField()
    contain = StringField()
    collected_from = StringField()
    title = StringField()
    frequency = StringField(choices=[e.value for e in FrequencyEnum], required=True)

    def __str__(self) -> str:
        return f"RunCollectRule<subject = {self.subject}, has_attachment = {self.has_attachment}" \
               f"export = {self.export}, mail_found_ids = {self.mail_found_ids}"
