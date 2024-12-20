from mongoengine import EmbeddedDocument, IntField, DictField, StringField

class QuoteVersion(EmbeddedDocument):
    name = IntField(required=True, default=1)   
    data = DictField(required=False, default={})
    pdf_link = StringField(required=True,default="")