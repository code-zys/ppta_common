from datetime import datetime
from bson import ObjectId
from mongoengine import Document, BooleanField, EmbeddedDocumentField, IntField, signals

from .user_metadata import UserMetadata
from ..utils.utils import Utils


class BaseDocument(Document):
    """
        Base document class
    """
    created_at = IntField(required=True)
    updated_at = IntField(default=None)
    created_by = EmbeddedDocumentField(UserMetadata, default=None)  
    updated_by = EmbeddedDocumentField(UserMetadata, default=None)
    deleted    = BooleanField(default=False)
    deleted_at = IntField(default=None)
    deleted_by = EmbeddedDocumentField(UserMetadata)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Register the signal for this subclass if not already registered
        if not hasattr(self.__class__, '_signals_registered'):
            self.__class__.register_signals()
            self.__class__._signals_registered = True

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        """Set created_at and updated_at before saving the document."""
        print('Pre save method is called')
        if hasattr(document, 'created_at'):
            if not document.created_at:
                document.created_at = Utils.convert_date_in_gmt_and_timstamp(datetime.now())
                document.updated_at = document.created_at
            else:
                document.updated_at = Utils.convert_date_in_gmt_and_timstamp(datetime.now())

    @classmethod
    def register_signals(cls):
        """Register pre_save signal for the subclass."""
        signals.pre_save.connect(cls.pre_save, sender=cls)

    meta = {
        'abstract': True,  # This makes the base class abstract
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
    
