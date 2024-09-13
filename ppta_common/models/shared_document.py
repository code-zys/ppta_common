from mongoengine import  IntField, ReferenceField, BooleanField
from .user import User
from .company import Company
from .base_document import BaseDocument

class SharedDocument(BaseDocument):
    user = ReferenceField(User)
    company =  ReferenceField(Company)
    month = IntField()
    year = IntField()
    read_only = BooleanField(default=True)

    meta = {
            'collection': 'shared_document'        
        }
    
    def __str__(self):
        return str(self.id)