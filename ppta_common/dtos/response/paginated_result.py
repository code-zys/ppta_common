from typing import TypeVar, Generic, List

from pydantic import BaseModel

DataT = TypeVar("DataT")


class PaginatedResult(BaseModel, Generic[DataT]):
    items: List[DataT]
    total_items: int  # Total count of items
    total_pages: int  # Total number of pages
    page: int  # Current page
    limit: int  # Items per page

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
        "from_attributes": True,
        "arbitrary_types_allowed": True
    }
