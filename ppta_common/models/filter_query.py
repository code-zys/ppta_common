from typing import Any, List, Optional
from pydantic import BaseModel


class Pagination(BaseModel):
    page: int = 1
    per_page: int = 25

class Sort(BaseModel):
    property: str
    direction: str = "asc"

class Expression(BaseModel):
    property: str
    operator: str
    values: Any

class FilterGroup(BaseModel):
    conditional: str = "and"
    expressions: List[Any] = []  # Can be `Expression` or `FilterGroup`

class QueryInput(BaseModel):
    search: Optional[str] = ""
    sort: Optional[Sort] = None
    pagination: Optional[Pagination] = None
    filter_group: Optional[FilterGroup] = None