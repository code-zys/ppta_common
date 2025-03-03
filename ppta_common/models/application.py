from .base_document import BaseDocument
from mongoengine import ReferenceField, StringField, IntField, BooleanField, EmbeddedDocumentField, ListField
from ..enums.application_status_enum import ApplicationStatus
from .company import Company
from .member import Member
from .answer import Answer
from ..enums.application_direction_enum import EnumApplicationDirection
from ..enums.generation_app_profile_status_enum import GenerationAppProfileStatus
from .application_match import ApplicationMatch
from .consultant import Consultant

class Application(BaseDocument):
    tender_call = ReferenceField("TenderCall", required=True)
    company = ReferenceField(Company, required=True)
    applicant_message = StringField(required=False)
    company_message = StringField(required=False)
    cv = StringField(required=True)
    application_status = StringField(choices=[e.value for e in ApplicationStatus], required=True)
    application_date = IntField(required=True)
    interview_completed = BooleanField(default=False)  
    applied_by_member = ReferenceField(Member, required=True)
    applied_for_consultant = ReferenceField(Consultant, required=True)
    origin = StringField(choices=[e.value for e in EnumApplicationDirection], required=True)
    matching = EmbeddedDocumentField(ApplicationMatch,required=False)
    answers = ListField(EmbeddedDocumentField(Answer),required=False)
    application_profile_s3_file_key = StringField(required=False)
    profile_status = StringField(choices=[e.value for e in GenerationAppProfileStatus], required=False)
    

    meta = {
        "collection": "applications",
        "strict": False,
        'indexes': [
            {
                'fields': ['company', 'tender_call','applied_for_member'],
                'unique': True 
            }
        ]
    }
