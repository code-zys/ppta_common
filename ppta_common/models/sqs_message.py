from .base_document import BaseDocument, EmbeddedDocumentField
from typing import Dict

class WkhtmltopdfOptions(EmbeddedDocumentField):
    orientation: str
    title: str
    margin: str

class SqsMessage(BaseDocument):
    source_bucket: str
    destination_bucket: str
    input_file_key: str
    wkhtmltopdf_options: WkhtmltopdfOptions
    data: Dict
    callback_url_success: str