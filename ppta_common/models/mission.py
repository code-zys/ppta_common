from mongoengine import StringField, DateTimeField, ReferenceField, EnumField
from .company import Company
from .member import Member
from .application import Application
from ..enums.mission_status_enum import MissionStatus
from .base_document import BaseDocument
from ..enums.mission_type_enum import MissionType

class Mission(BaseDocument):
    title = StringField(required=True)
    description = StringField()
    start_date = DateTimeField(required=True)
    end_date = DateTimeField()
    type = EnumField(MissionType, required=True, description="Type of the mission")
    company = ReferenceField(Company, required=True)

    
    consultant = ReferenceField(Member, required=False)
    consultant_original_company = ReferenceField(Company)
    
    commercial = ReferenceField(Member)
    commercial_company = ReferenceField(Company)

    client = ReferenceField(Company, required=False)

    status = EnumField(MissionStatus, required=True, description="Status of the mission", default=MissionStatus.PENDING)
    application = ReferenceField(Application,required=False)
    meta = {'collection': 'missions'}

    #TODO: all commercials in recruiter company can update those with tender call
    #TODO: for internal missions, only the commercial who is attached to it can update it