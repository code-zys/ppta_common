from typing import Optional
from pydantic import BaseModel

class CategoryCreateDto(BaseModel):
    name: str
    description: Optional[str] = None
    parent: Optional[str] = None