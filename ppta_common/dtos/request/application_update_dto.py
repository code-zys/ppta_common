from pydantic import BaseModel
from typing import Optional

class ApplicationUpdateDto(BaseModel):
    message: Optional[str] = None
    cv: Optional[str] = None 