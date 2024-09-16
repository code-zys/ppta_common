from datetime import datetime
from typing import Optional, ClassVar, List


from .extended_base_model import ExtendedBaseModel
from .process_rule_dto import ProcessRuleDto
from .run_invoice_dto import RunInvoiceDto
from ...enums.frequency_enum import FrequencyEnum
from ...enums.execution_status_enum import ExecutionStatusEnum


class RunProcessDto(ExtendedBaseModel):
    id: str= None
    user_id: Optional[str]= None
    plan_cron: Optional[str] = None
    name: Optional[str] = None
    run_date: Optional[datetime] = None
    run_month: Optional[int] = None
    run_year: Optional[int] = None
    process_rule: Optional[ProcessRuleDto] = None
    run_invoice_classes: List[RunInvoiceDto] = []
    status: Optional[ExecutionStatusEnum] = None 
    frequency: Optional[FrequencyEnum] = None 

    __properties: ClassVar[List[str]] = ["id", "plan_cron", "name",
                                         "run_date", "run_month", "run_year", "process_rule", "run_invoice_classes"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
        "from_attributes": True
    }
