from mongoengine import StringField, FloatField, IntField, BooleanField, ListField, EmbeddedDocumentField, EnumField, DateField, ReferenceField
from ppta_common.models.company import Company
from .base_document import BaseDocument
from ..enums.contract_type_enum import ContractType
from ..enums.experience_level_enum import ExperienceLevel
from .workplace import Workplace
from ..enums.remote_work_type_enum import RemoteWorkType
from ..enums.duration_type_enum import DurationType

class Mission(BaseDocument):
    job_title = StringField(required=True, description="Title of the job")
    slug = StringField(required=True, description="Title of the job")
    reference = StringField(required=True, description="Reference identifier for the mission")
    contract_type = EnumField(ContractType, required=True, description="Type of contract for the mission")
    min_daily_rate = FloatField(required=True, min_value=0, default=0)
    max_daily_rate = FloatField(required=True, min_value=0, default=0)
    min_annual_gross_salary = FloatField(required=True, min_value=0, default=0)
    max_annual_gross_salary = FloatField(required=True, min_value=0, default=0)
    is_remuneration_profile_based = BooleanField(required=True, description="Indicates if remuneration is based on the profile")
    experience = EnumField(ExperienceLevel, required=True, description="Experience level required for the mission")
    workplace = EmbeddedDocumentField(Workplace, required=True, description="Details about the workplace")
    start_date = DateField(description="Start date of the mission")
    starts_asap = BooleanField(required=True, description="Indicates if the mission starts as soon as possible")
    type_remote_work = EnumField(RemoteWorkType, required=True, description="Type of remote work available")
    job_description = StringField(required=True, description="Description of the job")
    expected_skills = ListField(StringField(), required=True, description="List of expected skills, e.g., AWS, Python, Pandas")
    know_how = ListField(StringField(), required=True, description="List of soft skills, e.g., communication, confidence")
    desired_profile = StringField(required=True, description="Description of the desired candidate profile")
    work_environment = StringField(required=True, description="Description of the work environment")
    company = ReferenceField(Company)
    created_by_company = ReferenceField(Company, required=False)
    duration = IntField(min_value=1, description="Duration of the mission")
    duration_type = EnumField(DurationType, required=True, description="Duration type: DAYS, MONTHS, YEARS")
    is_renewable = BooleanField(default=False, description="Indicates if the mission is renewable")
    currency = StringField(required=True)

    meta = {
        'collection': 'missions',
        'indexes': [
            {'fields': ['reference', 'company', 'slug'], 'unique': True},
        ],
        'strict': False
    }
