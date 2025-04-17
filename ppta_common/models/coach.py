from mongoengine import  StringField, ListField, BooleanField, IntField, EmbeddedDocumentField, ReferenceField, FloatField, EmbeddedDocumentListField
from .address import Address
from .language import Language
from .skill import Skill
from .base_document import BaseDocument
from .company import Company
from .workplaces import Workplace
from .timezone import TimeZone


class Coach(BaseDocument):
    """
    Coach model
    """
    name = StringField(max_length=50, required=True)
    email = StringField(max_length=50, required=True)
    phone = StringField(max_length=50, required=True)
    languages = ListField(EmbeddedDocumentField(Language), required=False)
    min_booking_time = IntField(required=False)
    workplaces = EmbeddedDocumentListField(Workplace, required=False) 
    member_id = StringField(required=False)
    is_coaching_profile_visible = BooleanField(default=True)
    is_profile_verified= BooleanField(default=False)
    is_profile_disabled_by_admin = BooleanField(default=False)
    company_approved_coach = BooleanField(default=True)
    company = ReferenceField(Company, required=True)
    bio = StringField(required=False)
    job_title = StringField(required=False)
    profile_picture = StringField(required=False)
    slug = StringField(required=False)
    address = EmbeddedDocumentField(Address, required=False)
    skills = ListField(EmbeddedDocumentField(Skill), required=False)
    hourly_rate = FloatField(required=False)
    price_id = StringField(required=True)
    timezone = EmbeddedDocumentField(TimeZone, required=True)
    stripe_account_id = StringField(required=False)
    has_set_up_stripe_connected_account = BooleanField(default=False)
    years_of_experience = IntField(required=True, default=0)
    
    meta = {
        'indexes': [
            'slug',
            'member_id',
            # nouvel index texte sur plusieurs champs
            {
                'fields': [
                    '$name',                # le champ name
                    '$bio',                 # le champ bio
                    '$skills.name',         # les compétences
                    '$workplaces.description'  # la description des workplaces
                ],
                'default_language': 'french',
                'weights': {
                    'name': 10,
                    'bio': 5,
                    'skills.name': 8,
                    'workplaces.description': 3
                }
            }
        ]
    }