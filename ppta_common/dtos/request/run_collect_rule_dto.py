from typing import Optional, List

from pydantic import Field

from ...enums.collect_rule_export_enum import CollectRuleExportEnum
from .extended_base_model import ExtendedBaseModel

class RunCollectRuleDto(ExtendedBaseModel):
    id: Optional[str] = None
    subject: Optional[str] = None
    from_: Optional[str] = Field(None, alias='from')
    has_attachment: Optional[bool] = None
    export: Optional[CollectRuleExportEnum] = None
    list_id_mail_found: Optional[List[str]] = None

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
        "from_attributes": True  # mandatory
    }
