from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, field_validator, validator
from ..response.user_meta_data_reponse import UserMetadataResponse


class ExtendedBaseModel(BaseModel):
    id: Optional[str]
    created_at: Optional[int] = None
    # created_by: Optional[dict] = None
    created_by: Optional[UserMetadataResponse] = None # TODO: NEW UPDATE
    

    @field_validator("id", mode="before")
    def transform_object_id_to_string(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value

