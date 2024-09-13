from mongoengine import Document, EmbeddedDocument, EnumField, StringField, FloatField, IntField, BooleanField, ReferenceField, ListField, EmbeddedDocumentField
from enum import Enum
from company import Company
from user_metadata import UserMetadata

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

