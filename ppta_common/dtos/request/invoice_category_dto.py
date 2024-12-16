from typing import List, Optional
from pydantic import BaseModel, validator
from ...enums.role_enum import EnumRole

class InvoiceCategoryDto(BaseModel):
    name: str
    code: str
    description: str
    is_system: bool