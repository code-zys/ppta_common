from mongoengine import StringField, EmbeddedDocumentField, BooleanField, ReferenceField, IntField, DictField, FloatField, ListField, EnumField
from .base_document import BaseDocument
from .company import Company
from .professional_info import ProfessionalInfo
from .user_metadata import UserMetadata
from .user import User
from ..utils.enums import EnumRole, EnumUserType
from .job import Job
from .skill import Skill
from .know_how import KnowHow
from .language import Language
from ..enums.experience_level_enum import ExperienceLevel

class Member(BaseDocument):
    professional_info = EmbeddedDocumentField(ProfessionalInfo, default=None)
    role = StringField(choices=[e.value for e in EnumRole], required=True)
    user = ReferenceField(User)
    firstname= StringField(required=False, description="The first name of the legar representant")
    lastname=StringField(required=False, description="The last name of the legar representant")
    company = ReferenceField(Company)
    approved = BooleanField(required=True)
    approved_at = IntField(default=None)
    approved_by = EmbeddedDocumentField(UserMetadata, default=None)
    user_type = StringField(choices=[e.value for e in EnumUserType], required=True)
    is_consultant = BooleanField(default=False)
    is_commercial = BooleanField(default=False)
    key_skills = DictField(EmbeddedDocumentField(Skill), required=False)
    general_skills=  DictField(EmbeddedDocumentField(Skill), required=False, description="The général skills of the member")
    know_how = DictField(EmbeddedDocumentField(KnowHow), required=False, description="List of soft skills, e.g., communication, confidence")
    job= EmbeddedDocumentField(Job, default=None)
    cv = StringField(required=False)
    other_cvs = ListField(StringField(), required=False, default = [])
    languages = ListField(EmbeddedDocumentField(Language))
    photo = StringField(required=False, description="The S3 key of the picture of the member")
    departments = ListField(StringField(), required=False,description="The list of departments were the member can work" )
    min_average_daily_rate = FloatField(required=False)
    max_average_daily_rate = FloatField(required=False)
    availability_date = IntField(required=False, description="The availability date of the member")
    years_of_experience = EnumField(ExperienceLevel, required=False, description="Experience level of the member")
    place_of_residence = StringField(required=False)
    is_coach = BooleanField(default=False, description="If the member is a coach and approved by the company")