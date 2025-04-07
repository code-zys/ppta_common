from mongoengine import FloatField, ReferenceField
from .base_document import BaseDocument
from .coach import Coach
from .coaching import Coaching

class EarningsByCoaching(BaseDocument):
    amount = FloatField(required=False)
    coach = ReferenceField(Coach, required=True)
    coaching = ReferenceField(Coaching, required=True)