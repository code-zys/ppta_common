from .mail_connection import MailConnection
from mongoengine import StringField, IntField,EmbeddedDocument, ReferenceField, EmbeddedDocumentField, DateTimeField, BooleanField

from .company import Company
from ..enums.token_type_enum import TokenTypeEnum
from ..utils.enums import EnumSecurityType
from ..enums.connection_category_enum import ConnectionCategoryEnum
class PrecomptaSherpaData(EmbeddedDocument):
    token = StringField(required=True)
    tokenType = StringField(choices=[e.value for e in TokenTypeEnum], default=TokenTypeEnum.BEARER)
    token_expiration_date = IntField(required=True)
    sherpa_user_id=StringField(required=True)
    enabled = BooleanField(required=False)


class Connection(MailConnection):
    host = StringField(required=False)
    port = IntField(required=False)
    user_name = StringField(required=False)
    password = StringField(required=False)
    security_type = StringField(choices=[e.value for e in EnumSecurityType], default=None)
    password = StringField(required=False)
    title = StringField(required=False)
    provider = StringField(required=False)
    user_id = StringField(required=False)
    email = StringField(required=False)
    access_token = StringField(required=False)
    refresh_token = StringField(required=False)
    company =  ReferenceField(Company, default=None)
    category = StringField(choices=[e.value for e in ConnectionCategoryEnum], default=None)
    name_folder = StringField(required=False)
    precompta_sherpa = EmbeddedDocumentField(PrecomptaSherpaData)

    def __repr__(self):
        return (f"Connection(title={self.title!r}, provider={self.provider!r}, category={self.category},"
                f"email={self.email!r}, host={self.host!r}, port={self.port!r}, "
                f"user_name={'***' if self.user_name else None}, "
                f"last_connection_status={self.last_connection_status!r}, "
                f"created_at={self.created_at}, updated_at={self.updated_at})")

    def __str__(self):
        return self.__repr__()