from mongoengine import FloatField, ReferenceField
from coaching import Coaching 
from coach import Coach
from .base_document import BaseDocument

class OrderHistory(BaseDocument):
    amount = FloatField(required=False)
    coach = ReferenceField(Coach, description="The coach concerned")
    coaching = ReferenceField(Coaching, description="L'activité de coaching pour laquelle le coach est payé")