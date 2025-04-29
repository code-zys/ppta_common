from bson import ObjectId
from mongoengine import Document, EmbeddedDocument, EnumField, StringField, FloatField, IntField, BooleanField, ReferenceField, ListField, EmbeddedDocumentField
from enum import Enum
from .company import Company
from .user_metadata import UserMetadata
from datetime import datetime

class EnumBilling(Enum):
    MONTHLY = "monthly"
    ANNUAL = "annual"

class EnumSubscriptionStatus(Enum):
    ACTIVE = "active"
    CANCELED = "canceled"
    EXPIRED = "expired"

class EnumBillingPeriod(Enum):
    MONTHLY = "monthly"
    ANNUAL = "annual"

class PlanMetadata(EmbeddedDocument):
    name = StringField(required=True)
    code = StringField(required=True)
    version = StringField(required=True)
    price = FloatField(required=True)

class Subscription(Document):
    billing = EnumField(EnumBilling, required=False)
    stripe_sub_id = StringField(required=False)
    taxRate = FloatField(required=True)
    taxAmount = FloatField(required=False)
    expiry = IntField(required=False)
    trailPeriodStartDate = IntField(required=False)
    trailPeriodEndDate = IntField(required=False)
    currentPeriodStart = IntField(required=False)
    currentPeriodEnd = IntField(required=False)
    status = EnumField(EnumSubscriptionStatus, required=False)
    payment = ListField(ReferenceField('payment'))
    company = ReferenceField(Company)
    plan = EmbeddedDocumentField(PlanMetadata, required=False)
    period = EnumField(EnumBillingPeriod, required=True)
    user = EmbeddedDocumentField(UserMetadata, required=False)
    cancel_at_period_end = BooleanField(required=False)
    cancelReason = StringField(required=False)



    meta = {'collection': 'subscriptions',
            'strict': False
        }
    
    def to_dict(self):
        data = self.to_mongo().to_dict()
        def convert_object_id(value):
            if isinstance(value, ObjectId):
                return str(value)
            elif isinstance(value, datetime):
                return value.isoformat()
            elif isinstance(value, dict):
                return {k: convert_object_id(v) for k, v in value.items()}
            elif isinstance(value, list):
                return [convert_object_id(v) for v in value]
            else:
                return value

        data = convert_object_id(data)

        # Replace the _id field with id
        if '_id' in data:
            data['id'] = data.pop('_id')

        return data

