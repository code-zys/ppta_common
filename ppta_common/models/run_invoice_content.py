from mongoengine import StringField, ListField, IntField, DateTimeField, ReferenceField, EnumField, DictField, BooleanField, EmbeddedDocumentField

from .base_document import BaseDocument
from ..utils.enums import FrequencyEnum
from ..enums.invoice_ocr_status_enum import InvoiceOcrStatus
from ..models.invoice_ocr import InvoiceOCR
from .company import Company
from .category import Category
from .user_metadata import UserMetadata
from .total import Totals
from .invoice_reconciliation import InvoiceReconciliation
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
    synchro_history = ListField(DictField())
    proprietor = ReferenceField("Member", default=None)
    validated = BooleanField(default=False)
    date_validated = IntField(default=None)
    ocr_status = StringField(choices=[status.value for status in InvoiceOcrStatus], default=None)
    ocr_started_at = DateTimeField()
    ocr_end_at = DateTimeField()
    ocr_data = EmbeddedDocumentField(InvoiceOCR)
    company = ReferenceField(Company)
    invoice_class_code = StringField()
    category = ReferenceField(Category, required=False)
    is_accepted = BooleanField(required=False)
    accepted_at = IntField(required=False)
    accepted_by = EmbeddedDocumentField(UserMetadata, default=None) 
    pricing = DictField(field=EmbeddedDocumentField(Totals), required=False, default={})
    reconciliations = ListField(EmbeddedDocumentField(InvoiceReconciliation, required=False, default=[]))

    
    def __str__(self):
        return f"RunInvoiceContent<file_path = {self.file_path}, run_invoice_id = {self.run_invoice_id}, invoice_received_date = {self.invoice_received_date}, ocr_data = {self.ocr_data}, subject = {self.subject}>"
