from mongoengine import StringField, ListField, IntField, DateTimeField, ReferenceField, EnumField

from .base_document import BaseDocument
from ..utils.enums import FrequencyEnum

class RunInvoiceContent(BaseDocument):
    """
    RunInvoiceContent document
    """
    file_path = StringField()
    file_name = StringField()
    file_size = IntField()
    frequency = EnumField(FrequencyEnum, required=True)
    file_extension = StringField()
    system_invoice_id = StringField()#ID OF INVOICE CLASS SYSTEM
    run_invoice_id = StringField()#ID OF RUN INVOICE CLASS
    run_process_id = StringField()
    invoice_received_date = DateTimeField()
    month = IntField()
    year = IntField()
    subject = StringField()
    company_id = StringField()
    sync_history = ListField(IntField())
    proprietor = ReferenceField("Member")

    def __str__(self):
        return f"RunInvoiceContent<file_path = {self.file_path}, run_invoice_id = {self.run_invoice_id}, invoice_received_date = {self.invoice_received_date}, subject = {self.subject}>"
