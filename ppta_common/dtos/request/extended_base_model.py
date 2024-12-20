from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, model_validator
from ..response.user_meta_data_reponse import UserMetadataResponse


class ExtendedBaseModel(BaseModel):
    id: Optional[str]
    created_at: Optional[int] = None
    # created_by: Optional[dict] = None
    created_by: Optional[UserMetadataResponse] = None # TODO: NEW UPDATE
    

    @model_validator(mode="before")
    def convert_objectids(cls, values):
        if hasattr(values, "to_dict") and callable(values.to_dict):
            values = values.to_dict()
            
        if isinstance(values, dict):
            for key, value in values.items():
                if isinstance(value, ObjectId):
                    values[key] = str(value)
        return values

