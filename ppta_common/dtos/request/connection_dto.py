from typing import Any, Dict, Optional
from pydantic import BaseModel

from utils.enums import EnumSecurityType
from ...enums.connection_category_enum import ConnectionCategoryEnum
from ...enums.token_type_enum import TokenTypeEnum


class PrecomptaSherpaDataDto:
    token: str
    token_type: TokenTypeEnum = TokenTypeEnum.BEARER
    token_expiration_date: int = 0
    sherpa_user_id= Optional[str]= ""

class ConnectionDto(BaseModel):
    title: Optional[str] = ""
    host: Optional[str] = ""
    port: Optional[int] = None
    user_name: Optional[str] = ""
    password: Optional[str] = ""
    security_type: Optional[EnumSecurityType] = None
    provider: Optional[str] = ""
    user_id: Optional[str] = ""
    email: Optional[str] = ""
    access_token: Optional[str] = ""
    refresh_token: Optional[str] = ""
    category: Optional[str] = ""
    precompta_sherpa: Optional[PrecomptaSherpaDataDto]


    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return (f"Connection(title={self.title!r}, provider={self.provider!r}, "
                f"email={self.email!r}, host={self.host!r}, port={self.port!r}, "
                f"user_name={'***' if self.user_name else None}")

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