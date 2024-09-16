from pydantic import BaseModel


class TestCollectRuleDto(BaseModel):
    year: int
    month: int