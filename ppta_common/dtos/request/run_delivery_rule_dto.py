from typing import Optional

from ...enums.delivery_rule_mode_enum import DeliveryRuleModeEnum
from .extended_base_model import ExtendedBaseModel


class RunDeliveryRuleDto(ExtendedBaseModel):
    """
        RunDeliveryruleDto
    """
    id: Optional[str] = None
    receiver: Optional[str] = None
    mode: Optional[str] = None
    receiver_mail: Optional[str] = None
    validate_before: Optional[bool] = None

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
        "from_attributes": True  # mandatory
    }