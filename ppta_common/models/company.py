
from mongoengine import StringField, EmbeddedDocumentField, BooleanField, IntField, ListField
from .address import Address
from .base_document import BaseDocument
from .timezone import TimeZone
from ..enums.company_type_enum import CompanyType
from ..utils.utils import Utils
from datetime import datetime

class Company(BaseDocument):
    siret = StringField(required=False)
    name = StringField(required=False)
    activity = StringField(required=False)
    type = StringField(choices=[e.value for e in CompanyType], required=True)
    timeZone = EmbeddedDocumentField(TimeZone, required=True)
    stripe_customer_id = StringField(required=False)
    subscription_id = StringField(required=False)
    member_count = IntField(required=True, default = 0)
    start_activity_date = IntField(default=Utils.convert_date_in_gmt_and_timstamp(datetime.now()))

    email = StringField(required=False)
    phone = StringField(required=False)
    address = EmbeddedDocumentField(Address)

    billing_email = StringField(required=False)
    billing_address = EmbeddedDocumentField(Address, default = None)
    use_contact_as_billing_info = BooleanField(default=False)
    payment_methods = ListField(StringField())
    contact_email = StringField(required=False)
    contact_phone_number = StringField(required=False)

    monthCountMember = IntField(required=True, default = 0)
    yearCountMember = IntField(required=True, default = 0)
    logo = StringField(required=False)
    bridge_user_uuid = StringField(required=False)
    currency = StringField(required=False)
    google_meet_agenda = StringField(required=False)