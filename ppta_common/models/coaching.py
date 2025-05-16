from mongoengine import StringField, BooleanField, ReferenceField, ListField, EmbeddedDocumentField
from .base_document import BaseDocument
from .session import Session
from .coach import Coach
from ..enums.coaching_category_enum import EnumCoachingCategory
from .basic_skill import BasicSkill
from .company import Company

class Coaching(BaseDocument):
    company = ReferenceField(Company, required=False) #TODO: To set to true
    coach = ReferenceField(Coach, required=True)
    workplace_code = StringField(required=False)
    workplace_name = StringField(required=False)
    category = StringField(choices=[e.value for e in EnumCoachingCategory], required=True)
    skills = ListField(EmbeddedDocumentField(BasicSkill), required=False)
    description = StringField(required=False)
    name = StringField(required=True)
    sessions = ListField(ReferenceField(Session), required=False)
    user = StringField(required=True) #TODO: To be removed
    is_cancelled = BooleanField(default=False)
    is_confirmed = BooleanField(default=False)
    invoice_links = ListField(StringField(),default=[],required=False)