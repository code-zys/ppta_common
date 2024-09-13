from datetime import date
from typing import Optional
from pydantic import BaseModel, validator

class CollectRuleDto(BaseModel):
    title: str
    subject: Optional[str] = None
    collected_from: Optional[str] = None
    has_attachment: bool
    before: str
    after: str
    contain: Optional[str] = None
    connection_id: str

@validator("has_attachment")
def validate_has_attachment(cls, value):
    if not value:
        raise ValueError("has_attachment ne peut pas être vide")
    return value

@validator("connection_id")
def validate_connexion_id(cls, value):
    if not value:
        raise ValueError("connexion_id ne peut pas être vide")
    return value

@validator("before")
def validate_before(cls, value):
    if not value:
        raise ValueError("before ne peut pas être vide")
    return value

@validator("after")
def validate_after(cls, value):
    if not value:
        raise ValueError("after ne peut pas être vide")
    return value
