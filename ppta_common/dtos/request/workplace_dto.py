from pydantic import BaseModel, Field


class WorkplaceDto(BaseModel):
    region: str = Field(..., description="Region where the workplace is located")
    town: str = Field(..., description="Town where the workplace is located")
