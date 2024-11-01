from mongoengine import StringField, ListField, BooleanField, \
    IntField, ReferenceField, EmbeddedDocumentField, EnumField

from .base_document import BaseDocument
from ..utils.enums import EnumRole, FrequencyEnum, InvoiceClassType
from .run_collect_rule import RunCollectRule
from .run_invoice_content import RunInvoiceContent
from .run_delivery_rule import RunDeliveryRule

class RunInvoiceClass(BaseDocument):
    """
    RunInvoiceClass
    """
    company_id = StringField()
    name = StringField()
    supplier = StringField()
    description = StringField()
    invoice_class_id = StringField()
    validate_before = BooleanField()
    month = IntField()
    year = IntField()
    code = StringField()
    type = EnumField(InvoiceClassType)
    frequency = EnumField(FrequencyEnum)
    run_process = ReferenceField("RunProcess")
    run_collect_rule = ListField(EmbeddedDocumentField(RunCollectRule))
    run_invoice_content = ListField(ReferenceField(RunInvoiceContent))
    run_delivery_rule = ListField(EmbeddedDocumentField(RunDeliveryRule))
    only_visible_by = ListField(StringField(choices=[e.value for e in EnumRole]), default = [])
    can_upload = ListField(StringField(choices=[e.value for e in EnumRole]), default = [])
    validated = BooleanField(default=False)
    date_validated = IntField(default=None)

    meta = {'collection': 'run_invoice_class',
            'indexes': [
                'company_id', 'deleted'  # Index on the company_id field
            ]}

    def __str__(self) -> str:
        return f"RunInvoiceClass<company_id = {self.company_id}, name = {self.name}," \
               f" validate_before = {self.validate_before}, run_collect_rule = {self.run_collect_rule}" \
               f" run_invoice_content = {self.run_invoice_content}>"
