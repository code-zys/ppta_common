from mongoengine import StringField, BooleanField, DictField
from .base_document import BaseDocument
from ..enums.invoice_template_type_enum import EnumInvoiceTemplateType
from ..enums.invoice_category_enum import InvoiceCategoryType
from ..enums.invoice_template_format_type_enum import EnumInvoiceTemplateFormatType

class InvoiceTemplate(BaseDocument):
    name = StringField(required=True, default="")
    description = StringField()
    source = StringField(required=True)
    front_source = StringField(required=False,default="basic/front.html")
    pdf_link = StringField()
    company_id = StringField(required=False,default=None)
    type  = StringField(choices=[e.value for e in EnumInvoiceTemplateType], required=True, default=EnumInvoiceTemplateType.STANDARD.value)
    format  = StringField(choices=[e.value for e in EnumInvoiceTemplateFormatType], required=True, default=EnumInvoiceTemplateFormatType.A4.value)
    is_default = BooleanField(default=False)
    category = StringField(choices=[e.value for e in InvoiceCategoryType], required=True, default=InvoiceCategoryType.INVOICE.value)
    isSystem = BooleanField(default=False)
    preview_image = StringField(required=True, default="")
    template_fields = DictField(required=False, default={})
    meta = {
        'collection': 'invoice_template',
        "strict": False
    }