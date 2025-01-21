from .base_document import BaseDocument
from mongoengine import (
    ReferenceField,
    ListField,
    StringField,
    FloatField
)
from ..enums.application_match_type_enum import ApplicationMatchType


class ApplicationMatch(BaseDocument):
    company = ReferenceField("Company", required=True)
    member = ReferenceField("Member", required=True)
    mission = ReferenceField("Mission", required=True)
    skills = ListField(StringField(max_length=100), required=True)
    percentage_match = FloatField(min_value=0, max_value=100, required=True)
    type = StringField(choices=[e.value for e in ApplicationMatchType], required=True)


    meta = {
        "collection": "application_matches",
        "indexes": [
            "company",
            "member",
            "mission",
            "percentage_match",
            "type",
        ],
    }