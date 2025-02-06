from pydantic import BaseModel
from typing import Dict

class WkhtmltopdfOptions(BaseModel):
    orientation: str
    title: str
    margin: str

class SqsMessage(BaseModel):
    source_bucket: str
    destination_bucket: str
    input_file_key: str
    wkhtmltopdf_options: WkhtmltopdfOptions
    data: Dict
    callback_url_success: str