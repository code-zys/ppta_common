from pydantic import BaseModel


class TimezoneDto(BaseModel):
    name: str
    offset: int