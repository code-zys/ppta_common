from pydantic import BaseModel, Field
from typing import Optional, Dict
from enum import Enum
from ...enums.filter_type_enum import EnumFilterType


class FilterDto(BaseModel):
    name: str = Field(..., title="Name of the filter")
    type: EnumFilterType = Field(..., title="Type of the filter", description="The type must be one of the predefined filter types")
    payload: Optional[Dict] = Field(None, title="Payload", description="Additional filter data")
