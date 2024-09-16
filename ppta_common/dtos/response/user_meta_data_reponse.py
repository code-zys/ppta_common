import json
import pprint
from typing import Optional
from pydantic import BaseModel
from typing import List, Optional, Self, Dict, Any, ClassVar

class UserMetadataResponse(BaseModel):
    id: Optional[str] = None
    fullname: Optional[str] = None
    picture: Optional[str] = None
    user_id: Optional[str] = None
    email: Optional[str] = None

    model_config = {
            "populate_by_name": True,
            "validate_assignment": True,
            "protected_namespaces": (),
            "from_attributes": True,
            "arbitrary_types_allowed": True
        }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AccountDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

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
 
    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProcessRuleDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "fullname": obj.get("fullname"),
            "picture": obj.get("picture"),
            "user_id": obj.get("user_id"),
            "email": obj.get("email"),
            # "launchable_manual": obj.get(" launchable_manual")
        })
        return _obj