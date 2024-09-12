"""
    models module
"""
from datetime import datetime

from mongoengine import Document, StringField, ListField, BooleanField, \
    DateField, ReferenceField, DateTimeField, \
    EmbeddedDocument, EnumField, EmbeddedDocumentField, IntField, DictField, ObjectIdField, signals
from bson import ObjectId
from .dto.invoice_class_type import InvoiceClassType
from .dto.collect_rule_export_enum import CollectRuleExportEnum
from .dto.delivery_rule_mode_enum import DeliveryRuleModeEnum
from .dto.execution_status_enum import ExecutionStatusEnum
from .dto.frequency_enum import FrequencyEnum
from enum import Enum

#from .dto.enum_security_type import EnumSecurityType
from .dto.enum_security_type import EnumSecurityType
from .dto.role_enum import EnumRole
from .dto.user_meta_data import UserMetadata

from .utils.utils import Utils
from .dto.export_type_enum import ExportType

class EnumConnectionStatus(str, Enum):
    NOT_TESTED = 'NOT_TESTED'
    SUCCESSFULLY_TESTED = 'TESTED_SUCCESSFULLY'
    FAILED_TEST = 'FAILED_TEST'


class BaseDocument(Document):
    """
        Base document class
    """
    created_at = IntField(required=True)
    updated_at = IntField(default=None)
    deleted = BooleanField(default=False)
    deleted_at = IntField(default=None)
    created_by = EmbeddedDocumentField(UserMetadata, default=None)  
    updated_by = EmbeddedDocumentField(UserMetadata, default=None)
    deleted_by = EmbeddedDocumentField(UserMetadata, default=None)

    meta = {
        'abstract': True,  # This makes the base class abstract
    }

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
            else:
                document.updated_at = Utils.convert_date_in_gmt_and_timstamp(datetime.now())

    @classmethod
    def register_signals(cls):
        """Register pre_save signal for the subclass."""
        signals.pre_save.connect(cls.pre_save, sender=cls)

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


class ProcessRule(BaseDocument):
    """
    ProcessRule document
    """
    company_id = StringField()
    plan_cron = StringField() # permet uniquement de déterminer le next_execution_date
    next_execution_date = DateField(required = False, default=None) 
    run_day = StringField() # permet de definir le jour pour une exécution mensuelle et annuelle et donc fabriquer le cron
    run_month = IntField() # permet de definir le jour pour une exécution annuelle et sert à fabriquer le cron
    # run_year = IntField()
    next_year = IntField(required = True) # next_year et next_month permettent de déterminer pour quelle periode la collecte est faite
    next_month = IntField()
    frequency = StringField(choices=[e.value for e in FrequencyEnum], required=True)
    # launchable_manual = BooleanField(default=False)
    name = StringField()
    invoice_class_ids = ListField(StringField())
    all_invoice = BooleanField(default=False)
    enabled = BooleanField(default=True)
    override = BooleanField()
    meta = {'collection': 'process_rule',
            'indexes': [
                'company_id', 'deleted'  # Index on the company_id field
            ]
            }

    def __str__(self):
        return f"ProcessRule<company_id = {self.company_id}, plan_cron = {self.plan_cron}, " \
               f"name = {self.name}, next_execution_date = {self.next_execution_date}, override = {self.override}," \
               f"invoice_class_ids ={self.invoice_class_ids}, all_invoice = {self.all_invoice}>"


class RunCollectRule(EmbeddedDocument):
    """
    RunCollectRule document
    """
    # from_ = StringField(db_field="from")
    subject = StringField()
    has_attachment = BooleanField()
    # has_word = ListField(StringField())
    export = EnumField(ExportType, default=ExportType.BODY)
    mail_found_ids = ListField(StringField())
    before = DateTimeField()
    after = DateTimeField()
    invoice_id = StringField()
    connection_id = StringField()
    contain = StringField()
    collected_from = StringField()
    title = StringField()
    frequency = StringField(choices=[e.value for e in FrequencyEnum], required=True)

    def __str__(self) -> str:
        return f"RunCollectRule<subject = {self.subject}, has_attachment = {self.has_attachment}" \
               f"export = {self.export}, mail_found_ids = {self.mail_found_ids}"

class RunDeliveryRule(EmbeddedDocument):
    """
    RunDeliveryRule document
    """
    mode = EnumField(DeliveryRuleModeEnum, default=DeliveryRuleModeEnum.API)
    receiver = StringField()
    receiver_mail = StringField()

    def __str__(self):
        return f"RunDeliveryRule<mode = {self.mode}, receiver = {self.receiver}, receiver_mail = {self.receiver_mail}>"


class RunInvoiceContent(BaseDocument):
    """
    RunInvoiceContent document
    """
    file_path = StringField()  # S3 object key
    file_name = StringField()
    file_size = IntField()
    frequency = StringField(choices=[e.value for e in FrequencyEnum], required=True)
    file_extension = StringField()
    system_invoice_id = StringField()#ID OF INVOICE CLASS SYSTEM
    run_invoice_id = StringField()#ID OF RUN INVOICE CLASS
    run_process_id = StringField() #TODO: check if useful if not remove
    invoice_received_date = DateTimeField()
    month = IntField()
    year = IntField()
    subject = StringField()
    company_id = StringField()
    sync_history = ListField(IntField())
    synchro_history = ListField(DictField())
    proprietor = ReferenceField("Member")

    def __str__(self):
        return f"RunInvoiceContent<file_path = {self.file_path}, run_invoice_id = {self.run_invoice_id}, invoice_received_date = {self.invoice_received_date}, subject = {self.subject}>"

class RunInvoiceClass(BaseDocument):
    """
    RunInvoiceClass
    """
    company_id = StringField()
    name = StringField()
    supplier = StringField()
    description = StringField()
    invoice_class_id = StringField()
    validate_before = BooleanField()
    month = IntField()
    year = IntField()
    code = StringField()
    type = StringField(choices=[e.value for e in InvoiceClassType])
    frequency = StringField(choices=[e.value for e in FrequencyEnum])
    run_process = ReferenceField("RunProcess")
    run_collect_rule = ListField(EmbeddedDocumentField(RunCollectRule))
    run_invoice_content = ListField(ReferenceField(RunInvoiceContent))
    run_delivery_rule = ListField(EmbeddedDocumentField(RunDeliveryRule))

    meta = {'collection': 'run_invoice_class',
            'indexes': [
                'company_id', 'deleted'  # Index on the company_id field
            ]}

    def __str__(self) -> str:
        return f"RunInvoiceClass<company_id = {self.company_id}, name = {self.name}," \
               f" validate_before = {self.validate_before}, run_collect_rule = {self.run_collect_rule}" \
               f" run_invoice_content = {self.run_invoice_content}>"


class RunProcess(BaseDocument):
    """
    RunProcessDocument document
    """
    company_id = StringField()
    plan_cron = StringField()
    name = StringField()
    run_date = DateField(default=datetime.now())
    run_month = IntField()
    run_year = IntField()
    # frequency: FrequencyEnum
    process_rule = ReferenceField(ProcessRule)
    override = BooleanField(default=False)
    run_invoice_classes = ListField(ReferenceField(RunInvoiceClass))
    merge_list = ListField(IntField())
    status = StringField(choices=[e.value for e in ExecutionStatusEnum], required=True)
    frequency = StringField(choices=[e.value for e in FrequencyEnum], required=True)

    meta = {'collection': 'run_process',
            'indexes': ['company_id', 'run_month', 'run_year', 'deleted']
            }

    def __str__(self):
        return f"RunProcess<plan_cron = {self.plan_cron}, name = {self.name}, " \
               f"run_date ={self.run_date}, run_month = {self.run_month}, run_year={self.run_year}, process_rule = {self.process_rule}, status = {self.status}, frequency = {self.frequency}>" #TODO:
            #    f"run_date ={self.run_date}, run_month = {self.run_month}, run_year={self.run_year}, process_rule = {self.process_rule}>" #TODO:

class MailConnection(BaseDocument):
    type = StringField(required=True)
    title = StringField(required=True)
    last_connection_date = IntField(default=None)
    last_connection_status = StringField(choices=[e.value for e in EnumConnectionStatus], default=EnumConnectionStatus.NOT_TESTED)

    meta = {
        'abstract': True,  # This makes the base class abstract
    }

class InvoiceClass(BaseDocument):
    supplier = StringField(required=True)
    name = StringField(required=True)
    description = StringField()
    company_id = ObjectIdField()
    code = StringField()
    ##run_invoice_content = ListField(ReferenceField(RunInvoiceContent)) # cet  attribut n'est pas utilisé
    type = StringField(choices=[e.value for e in InvoiceClassType], required=True)
    meta = {'collection': 'invoice',
             'strict': False
            }
    
    def __str__(self):
        return str(self.id)
    
class User(Document):
    # id = ObjectIdField(required=True)
    meta = {
        'collection': 'users',
        "strict": False
    }
    firstname = StringField(required=False, default="")
    lastname = StringField(required=False, default="")
    picture = StringField(required=False, default="")
    userId = StringField(required=False, default="")
    email = StringField(required=False, default="")

class Company(Document):
    meta = {
        'collection': 'company',
        "strict": False
    }
    name = StringField(required=False, default="")
    
class SharedDocument(BaseDocument):
    user = ReferenceField(User)
    company =  ReferenceField(Company)
    month = IntField()
    year = IntField()
    read_only = BooleanField(default=True)
    meta = {'collection': 'shared_document',
             'strict': False
            }
    
    def __str__(self):
        return str(self.id)
    

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
    category = StringField(required=False)
    name_folder = StringField(required=False)

    def __repr__(self):
        return (f"Connection(title={self.title!r}, provider={self.provider!r}, "
                f"email={self.email!r}, host={self.host!r}, port={self.port!r}, "
                f"user_name={'***' if self.user_name else None}, "
                f"last_connection_status={self.last_connection_status!r}, "
                f"created_at={self.created_at}, updated_at={self.updated_at})")

    def __str__(self):
        return self.__repr__()

class UserMetadata(EmbeddedDocument):
    id = StringField()
    fullname = StringField()
    picture = StringField(default="")
    user_id = StringField()
    email = StringField()

class CollectRule(EmbeddedDocument):
    id = StringField()
    subject = StringField()
    title = StringField()
    collected_from = StringField()
    to = StringField()
    has_attachment = BooleanField()
    has_word = BooleanField()
    before = StringField()
    after = StringField()
    contain = StringField()
    search = StringField()
    connection_id = StringField()
    export = EnumField(ExportType)
    invoice_id = StringField()
    created_at = IntField(required=True)
    updated_at = IntField(default=None)

    last_connection_date = IntField(default=None)
    last_connection_status = StringField(choices=[e.value for e in EnumConnectionStatus], default=EnumConnectionStatus.NOT_TESTED)

class DeliveryRule(EmbeddedDocument):
    id = StringField()
    title = StringField()
    receiver = StringField()
    mode = EnumField(DeliveryRuleModeEnum)
    receiver_mail = StringField()
    api = StringField()
    validate_before = BooleanField()
    invoice_id = StringField()

    created_at = IntField(required=True)
    updated_at = IntField(default=None)
    
class Invoice(BaseDocument):
    supplier = StringField()
    name = StringField()
    code = StringField()

    type = EnumField(InvoiceClassType)
    description = StringField()
   
    created_at = IntField(required=True)
    updated_at = IntField(default=None)
    deleted = BooleanField(default=False)
    deleted_at = IntField(default=None)
    created_by = EmbeddedDocumentField(UserMetadata, default=None)  
    updated_by = EmbeddedDocumentField(UserMetadata, default=None)
    deleted_by = EmbeddedDocumentField(UserMetadata, default=None)
    
    collect_rules = ListField(EmbeddedDocumentField(CollectRule))
    delivery_rules = ListField(EmbeddedDocumentField(DeliveryRule))
    company_id = ObjectIdField(required=True)


class ProfessionalInfo(EmbeddedDocument):
    work_station = StringField(required=True)
    phone_number = StringField(required=True)
    professional_email = StringField(required=True)
    start_date = DateTimeField(required=True)
    validation_date = DateTimeField(default=None)
    company_id = ObjectIdField(required=True)
    approved = BooleanField(required=True)


class EnumUserType(str, Enum):
    CERTIFIED_ACCOUNTANT = 'CERTIFIED_ACCOUNTANT'
    CONTRACTOR = 'CONTRACTOR'

class User(Document):
    meta = {
        'collection': 'users',
        "strict": False
    }
    firstname = StringField(required=False, default="")
    lastname = StringField(required=False, default="")
    picture = StringField(required=False, default="")
    userId = StringField(required=False, default="")
    email = StringField(required=False, default="")
    user_type = StringField(choices=[e.value for e in EnumUserType], required=True)
    professional_info = EmbeddedDocumentField(ProfessionalInfo, default=None)

class MemberInfo:
    memberId: str
    companyId: str
    userId: str
    role: EnumRole
    
    def __init__(self, companyId: str, userId: str, role: EnumRole, memberId: str):
        self.companyId = companyId
        self.userId = userId
        self.role = role
        self.memberId = memberId


class Member(BaseDocument):
    professional_info = EmbeddedDocumentField(ProfessionalInfo, default=None)
    role = StringField(choices=[e.value for e in EnumRole], required=True)
    user = ReferenceField(User)
    company = ReferenceField(Company)
    approved = BooleanField(required=True)
    approved_at = IntField(default=None)
    approved_by = EmbeddedDocumentField(UserMetadata, default=None) 
    user_type = StringField(choices=[e.value for e in EnumUserType], required=True)