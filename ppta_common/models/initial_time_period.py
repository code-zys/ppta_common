from mongoengine import  EmbeddedDocument, IntField

class InitialTimePeriod(EmbeddedDocument):
    """
    Initial time range model
    """
    start_time = IntField(required=True)
    end_time = IntField(required=True)