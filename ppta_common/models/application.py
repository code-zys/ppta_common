from .base_document import BaseDocument
from mongoengine import ReferenceField, StringField, IntField, BooleanField, EmbeddedDocumentField, ListField
from ..enums.application_status_enum import ApplicationStatus
from .company import Company
from .member import Member
from .answer import Answer
from ..enums.application_direction_enum import EnumApplicationDirection
from .application_match import ApplicationMatch

class Application(BaseDocument):
    mission = ReferenceField("Mission", required=True)
    company = ReferenceField(Company, required=True)
    applicant_message = StringField(required=False)
    company_message = StringField(required=False)
    cv = StringField(required=True)
    application_status = StringField(choices=[e.value for e in ApplicationStatus], required=True)
    application_date = IntField(required=True)
    interview_completed = BooleanField(default=False)  
    applied_by_member = ReferenceField(Member, required=True)
    applied_for_member = ReferenceField(Member, required=True)
    origin = StringField(choices=[e.value for e in EnumApplicationDirection], required=True)
    matching = EmbeddedDocumentField(ApplicationMatch,required=False)
    answers = ListField(EmbeddedDocumentField(Answer),required=False)

    meta = {
        "collection": "applications",
        "strict": False,
        'indexes': [
            {
                'fields': ['company', 'mission','applied_for_member'],
                'unique': True 
            }
        ]
    }
