from typing import Optional, TypeVar, Generic, Dict, Any, ClassVar, List

from pydantic import BaseModel

from utils.enums import EnumStatusResponse

DataT = TypeVar("DataT")


class RestResponse(BaseModel, Generic[DataT]):
    data: DataT
    message: Optional[str] = None
    status_code: int
    status_response: EnumStatusResponse
    __properties: ClassVar[List[str]] = ["data", "message", "status_code", "status_response"]


def to_dict(self) -> Dict[str, Any]:
    """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
    _dict = self.model_dump(
        by_alias=True,
        exclude={
        },
        exclude_none=True,
    )
    return _dict