from typing import Optional
from ...enums.delivery_rule_mode_enum import DeliveryRuleModeEnum
from pydantic import BaseModel, validator
class DeliveryRuleDto(BaseModel):
    title: str
    receiver: str
    mode: DeliveryRuleModeEnum
    receiver_mail: Optional[str] = ""
    api: Optional[str] = ""
    validate_before: bool
  
@validator("receiver")
def validate_receiver(cls, value):
    if not value:
        raise ValueError("receiver ne peut pas être vide")
    return value

@validator("mode")
def validate_mode(cls, value):
    if not value:
        raise ValueError("mode ne peut pas être vide")
    return value

@validator("validate_before")
def validate_validate_before(cls, value):
    if not value:
        raise ValueError("validate_before ne peut pas être vide")
    return value