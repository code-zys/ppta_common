from enum import Enum


class EnumStatusResponse(Enum):
    UNKNOWN = 'UNKNOWN'
    RECOVERED_SUCCESSFULLY = 'RECOVERED_SUCCESSFULLY'
    CREATED_SUCCESSFULLY = 'CREATED_SUCCESSFULLY'
    UPDATED_SUCCESSFULLY = 'UPDATED_SUCCESSFULLY'
    DELETED_SUCCESSFULLY = 'DELETED_SUCCESSFULLY'
    SAVED_SUCCESSFULLY = 'SAVED_SUCCESSFULLY'
    NO_CONTENT = 'NO_CONTENT'
    NOT_FOUND = 'NOT_FOUND'
    FORBIDDEN = 'FORBIDDEN'
    SENT_SUCCESSFULLY = 'SENT_SUCCESSFULLY'
    MAIL_SENDED_IN_QUEUE_SUCCESSFULLY='MAIL_SENDED_IN_QUEUE_SUCCESSFULLY'
    FAILED_TO_SEND_IN_QUEUE='FAILED_TO_SEND_IN_QUEUE'
    

class EnumUserType(str, Enum):
    CERTIFIED_ACCOUNTANT = 'CERTIFIED_ACCOUNTANT'
    CONTRACTOR = 'CONTRACTOR'

class EnumSatusInvitation(str, Enum):
    PENDING = 'PENDING'
    ACCEPTED = 'ACCEPTED'
    REFUSED = 'REFUSED'
    CANCELLED = 'CANCELLED'
    DELETED = 'DELETED'

class EnumRole(str, Enum):
    OWNER = 'OWNER'
    MANAGER = 'MANAGER'
    EMPLOYEE = 'EMPLOYEE'

class EnumOriginInvitation(str, Enum):
    FROM_USER_TO_COMPANY = 'FROM-USER-TO-COMPANY'
    FROM_COMPANY_TO_USER = 'FROM-COMPANY-TO-USER'
class ExportType(str, Enum):
  ATTACHMENT = "ATTACHMENT"
  BODY = "BODY"

class DeliveryRuleModeEnum(Enum):
    """
        Enum values
    """
    MAIL = 'MAIL'
    API = 'API'

# class InvoiceClassType(Enum):
#     INVOICE = 'INVOICE'
#     NOTE_DE_FRAIS = 'NOTE_DE_FRAIS'


class InvoiceClassType(str, Enum):
    #INVOICE = 'INVOICE'
    #NOTE_DE_FRAIS = 'NOTE_DE_FRAIS'

    STANDARD = 'STANDARD'
    SYSTEM = 'SYSTEM'

class EnumConnectionStatus(str, Enum):
    NOT_TESTED = 'NOT_TESTED'
    SUCCESSFULLY_TESTED = 'TESTED_SUCCESSFULLY'
    FAILED_TEST = 'FAILED_TEST'

class FrequencyEnum(str, Enum):
    ANNUAL = "ANNUAL"
    MONTHLY = "MONTHLY"
    PONTUAL = "PONTUAL"

class ExecutionStatusEnum(str, Enum):
    NOT_STARTED = 'NOT_STARTED'
    IN_PROGESS = 'IN_PROGESS'
    SUCCESSFULLY = 'SUCCESSFULLY'
    FAILED = 'FAILED'

class EnumSecurityType(str, Enum):
    SSL = 'SSL'
    TLS = 'TLS'
    NONE = 'None'