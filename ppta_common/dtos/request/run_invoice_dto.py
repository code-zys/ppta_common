from typing import Optional, List

from .extended_base_model import ExtendedBaseModel
from .run_collect_rule_dto import RunCollectRuleDto
from .run_delivery_rule_dto import RunDeliveryRuleDto
from ...utils.enums import InvoiceClassType

class RunInvoiceDto(ExtendedBaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    supplier: Optional[str] = None
    code: Optional[str] = None
    type: Optional[InvoiceClassType] = None
    invoice_class_id: Optional[str] = None
    # run_process: Optional[RunProcessDto]= None
    run_collect_rule: Optional[List[RunCollectRuleDto]] = []
    # run_invoice_content: Optional[List[RunInvoiceContentDto]] = []
    run_delivery_rule: Optional[List[RunDeliveryRuleDto]] = []
    validated: Optional[bool] = False
    date_validated: Optional[int] = None
    only_visible_by: Optional[list[str]] = []
    can_upload: Optional[list[str]] = []
    year: Optional[int] = None
    month: Optional[int] = None
    frequency: Optional[str] = None
    is_shared: Optional[bool] = False

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
        "from_attributes": True  # mandatory
    }
