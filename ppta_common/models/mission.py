from mongoengine import StringField, FloatField, IntField, BooleanField, ListField, EmbeddedDocumentField, EnumField, DateField, TupleField, ReferenceField
from ppta_common.models.company import Company
from .base_document import BaseDocument
from ..enums.contract_type_enum import ContractType
from ..enums.experience_level_enum import ExperienceLevel
from ..enums.know_how import KnowHow
from ..enums.skill_enum import Skill
from .workplace import Workplace
from ..enums.remote_work_type_enum import RemoteWorkType

class Mission(BaseDocument):
    job_title = StringField(required=True, description="Title of the job")
    reference = StringField(required=True, description="Reference identifier for the mission")
    contract_type = EnumField(ContractType, required=True, description="Type of contract for the mission")
    daily_rate = FloatField(min_value=0, description="Daily rate for freelance contracts")
    annual_gross_salary = TupleField(IntField(min_value=1), IntField(min_value=1), description="Annual gross salary range as a tuple of minimum and maximum")
    is_remuneration_profile_based = BooleanField(required=True, description="Indicates if remuneration is based on the profile")
    experience = EnumField(ExperienceLevel, required=True, description="Experience level required for the mission")
    workplace = EmbeddedDocumentField(Workplace, required=True, description="Details about the workplace")
    start_date = DateField(description="Start date of the mission")
    starts_asap = BooleanField(required=True, description="Indicates if the mission starts as soon as possible")
    type_remote_work = EnumField(RemoteWorkType, required=True, description="Type of remote work available")
    job_description = StringField(required=True, description="Description of the job")
    expected_skills = ListField(EnumField(Skill), required=True, description="List of expected skills, e.g., AWS, Python, Pandas")
    know_how = ListField(EnumField(KnowHow), required=True, description="List of soft skills, e.g., communication, confidence")
    desired_profile = StringField(required=True, description="Description of the desired candidate profile")
    work_environment = StringField(required=True, description="Description of the work environment")
    company = ReferenceField(Company)
    created_by_company = ReferenceField(Company, required=False)

    meta = {
        'collection': 'missions',
        'indexes': [
            {'fields': ['reference', 'company'], 'unique': True},
        ],
        'strict': False
    }
