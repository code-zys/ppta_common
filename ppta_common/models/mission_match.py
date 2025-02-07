from .base_document import BaseDocument
from mongoengine import (
    ReferenceField,
    ListField,
    StringField,
    FloatField
)
from ..enums.mission_match_type_enum import MissionMatchType
from .company import Company


class MissionMatch(BaseDocument):
    member_company = ReferenceField(Company, required=True)
    mission_company = ReferenceField(Company, required=True)
    member = ReferenceField("Member", required=True)
    tender_call = ReferenceField("TenderCall", required=True)
    mission_skills = ListField(StringField(max_length=100), required=True)
    percentage_match = FloatField(min_value=0, max_value=100, required=True)
    type = StringField(choices=[e.value for e in MissionMatchType], required=True)

    meta = {
        "collection": "mission_matches"
    }