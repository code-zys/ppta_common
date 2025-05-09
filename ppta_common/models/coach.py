from mongoengine import  StringField, ListField, BooleanField, IntField, EmbeddedDocumentField, ReferenceField, FloatField, EmbeddedDocumentListField
from .address import Address
from .language import Language
from .base_document import BaseDocument
from .company import Company
from .workplaces import Workplace
from .timezone import TimeZone
from .basic_skill import BasicSkill
from .skill import Skill

class Coach(BaseDocument):
    """
    Coach model
    """
    name = StringField(max_length=50, required=True)
    email = StringField(max_length=50, required=True)
    phone = StringField(max_length=50, required=True)
    languages = ListField(EmbeddedDocumentField(Language), required=False)
    min_booking_time = IntField(required=False)
    workplaces = EmbeddedDocumentListField(Workplace, required=False)  #TODO: To be removed 
    member_id = StringField(required=False)
    is_coaching_profile_visible = BooleanField(default=True)
    is_profile_verified= BooleanField(default=False)
    is_profile_disabled_by_admin = BooleanField(default=False)
    company_approved_coach = BooleanField(default=True)
    company = ReferenceField(Company, required=True)
    skills = ListField(EmbeddedDocumentField(Skill), required=False) #TODO: To be removed 
    bio = StringField(required=False)
    job_title = StringField(required=False)
    profile_picture = StringField(required=False)
    slug = StringField(required=False)
    address = EmbeddedDocumentField(Address, required=False)
    hourly_rate = FloatField(required=False) #TODO: To be removed 
    timezone = EmbeddedDocumentField(TimeZone, required=True)
    stripe_account_id = StringField(required=False)
    has_set_up_stripe_connected_account = BooleanField(default=False)
    years_of_experience = IntField(required=True, default=0)
    verified_at = IntField(required=False)
    average_rating = FloatField(required=False, default=0)
    total_raters = IntField(required=False, default=0) #TODO: To be removed, Add an endpoint to get the total raters
    
    mission_support = BooleanField(default=False)
    mission_workplace = EmbeddedDocumentListField(Workplace, required=False)
    mission_another_pricing = FloatField(required=False, description="Pricing for other participants")
    mission_default_pricing = FloatField(required=False, description="Default price for the first person") 
    
    interview_support = BooleanField(default=False)
    interview_workplace = EmbeddedDocumentListField(Workplace, required=False)
    interview_another_pricing = FloatField(required=False)
    interview_default_pricing = FloatField(required=False)
    
    communication_support = BooleanField(default=False)
    communication_description = StringField(required=False)
    communication_another_pricing = FloatField(required=False)
    communication_default_pricing = FloatField(required=False)
    
    it_support = BooleanField(default=False)
    it_skills = ListField(EmbeddedDocumentField(BasicSkill), required=False)
    it_another_pricing = FloatField(required=False)
    it_default_pricing = FloatField(required=False)
    
    other_support = BooleanField(default=False)
    other_title = StringField(required=False)
    other_description = StringField(required=False)
    other_another_pricing = FloatField(required=False)
    other_default_pricing = FloatField(required=False)
    
    meta = {
        'indexes': [
            'slug',
            'member_id',
            # nouvel index texte sur plusieurs champs
            {
                'fields': [
                    '$name',                # le champ name
                    '$bio',                 # le champ bio
                    '$it_skills.name',         # les compétences
                    '$workplaces.description'  # la description des workplaces
                ],
                'default_language': 'french',
                'weights': {
                    'name': 10,
                    'bio': 5,
                    'it_skills.name': 8,
                    'workplaces.description': 3
                }
            }
        ]
    }