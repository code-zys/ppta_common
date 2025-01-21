from .base_document import BaseDocument
from mongoengine import ReferenceField, URLField, StringField, IntField, BooleanField
from ..enums.application_status_enum import ApplicationStatus
from .company import Company
from .mission import Mission
from .member import Member

class Application(BaseDocument):
    mission = ReferenceField(Mission, required=True)
    company = ReferenceField(Company, required=True)
    message = StringField(required=True)
    cv = URLField(required=True)
    application_status = StringField(choices=[e.value for e in ApplicationStatus], required=True)
    application_date = IntField(required=True)
    interview_completed = BooleanField(default=False)  
    applied_by_member = ReferenceField(Member, required=True)
    applied_for_member = ReferenceField(Member, required=True)

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
