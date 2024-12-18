
from enum import Enum

class EnumStatusCode(Enum):
    UNKNOWN = 'UNKNOWN'
    RECOVERED_SUCCESSFULLY = 'RECOVERED_SUCCESSFULLY'
    CREATE_URL_SUCCESSFULLY = 'CREATE_URL_SUCCESSFULLY'
    CREATED_SUCCESSFULLY = 'CREATED_SUCCESSFULLY'
    UPDATED_SUCCESSFULLY = 'UPDATED_SUCCESSFULLY'
    DELETED_SUCCESSFULLY = 'DELETED_SUCCESSFULLY'
    TESTED_SUCCESSFULLY = 'TESTED_SUCCESSFULLY'
    CONNECTION_SUCCESSFULLY = 'CONNECTION_SUCCESSFULLY'
    NO_CONTENT = 'NO_CONTENT'
    NOT_FOUND = 'NOT_FOUND'
    RUN_INVOICE_CONTENT_NOT_FOUND = 'RUN_INVOICE_CONTENT_NOT_FOUND'
    RUN_INVOICE_CLASS_NOT_FOUND = 'RUN_INVOICE_CLASS_NOT_FOUND'
    RUN_INOICE_CONTENT_ALREADY_IN_INVOICE_CLASS = 'RUN_INOICE_CONTENT_ALREADY_IN_INVOICE_CLASS'
    INVOICE_CLASS_SYSTEM_NOT_FOUND = 'INVOICE_CLASS_SYSTEM_NOT_FOUND'
    INVOICE_CLASS_IS_NOT_AN_INVOICE_CLASS_SYSTEM = 'INVOICE_CLASS_IS_NOT_AN_INVOICE_CLASS_SYSTEM'
    ID_INVOICE_CLASS_HAS_NOT_SPECIFIED = 'ID_INVOICE_CLASS_HAS_NOT_SPECIFIED'
    INVOICE_CLASS_MOVED_SUCCESSFULLY = 'INVOICE_CLASS_MOVED_SUCCESSFULLY'
    COMPANY_NOT_FOUND = 'COMPANY_NOT_FOUND'
    COMPANY_ALREADY_EXIST = 'COMPANY_ALREADY_EXIST'
    MEMBER_NOT_FOUND = 'MEMBER_NOT_FOUND'
    FORBIDDEN= 'FORBIDDEN'
    MEMBER_NOT_CREATED= "MEMBER_NOT_CREATED"
    INVITATION_ALREADY_EXIST = "INVITATION_ALREADY_EXIST"
    INVITATION_ACCEPTED = "INVITATION_ACCEPTED"
    SENT_SUCCESSFULLY = 'SENT_SUCCESSFULLY'
    MAIL_SENDED_IN_QUEUE_SUCCESSFULLY='MAIL_SENDED_IN_QUEUE_SUCCESSFULLY'
    FAILED_TO_SEND_IN_QUEUE='FAILED_TO_SEND_IN_QUEUE'
    INVALID_REQUEST = "INVALID_REQUEST"
    COMPANY_SIRET_ALREADY_EXIST = 'COMPANY_SIRET_ALREADY_EXIST'
    COMPANY_SIREN_ALREADY_EXIST = 'COMPANY_SIREN_ALREADY_EXIST'
    USER_NOT_FOUND = 'USER_NOT_FOUND'
    SOUSCRIPTION_NOT_FOUND = 'SOUSCRIPTION_NOT_FOUND'
    USER_IS_ALREADY_MEMBER_OF_COMPANY = 'USER_IS_ALREADY_MEMBER_OF_COMPANY'
    USER_IS_NOT_A_CERTIFIED_ACCOUNTANT = 'USER_IS_NOT_A_CERTIFIED_ACCOUNTANT'
    INVITATION_NOT_FOUND = 'INVITATION_NOT_FOUND'
    SHARED_SUCCESSFULLY = 'SHARED_SUCCESSFULLY'
    SHARED_DOCUMENT_NOT_FOUND = 'SHARED_DOCUMENT_NOT_FOUND'
    DOCUMENT_ALREADY_SHARED_WITH_USER = 'DOCUMENT_ALREADY_SHARED_WITH_USER'
    START_ACTIVITY_DATE_CANNOT_BE_GREATER_THAN_CREATE_COMPANY_DATE = 'START_ACTIVITY_DATE_CANNOT_BE_GREATER_THAN_CREATE_COMPANY_DATE'
    START_ACTIVITY_DATE_EXTENDED_SUCCESSFULLY = 'START_ACTIVITY_DATE_EXTENDED_SUCCESSFULLY'
    MEMBER_APPROVED_SUCCESSFULLY = 'MEMBER_APPROVED_SUCCESSFULLY'
    INVOICE_CLASS_NOT_FOUND = 'INVOICE_CLASS_NOT_FOUND'
    CONNECTION_NOT_FOUND = 'CONNECTION_NOT_FOUND'
    AFTER_IS_NOT_VALID = 'AFTER_IS_NOT_VALID'
    BEFORE_IS_NOT_VALID = 'BEFORE_IS_NOT_VALID'
    INVOICE_CLASS_ALREADY_EXIST = 'INVOICE_CLASS_ALREADY_EXIST'
    DELIVERY_RULE_NOT_FOUND = 'DELIVERY_RULE_NOT_FOUND'
    INVOICE_ALREADY_EXISTS = 'INVOICE_ALREADY_EXISTS'
    RUN_INVOICE_CLASS_UPDATED = 'RUN_INVOICE_CLASS_UPDATED'
    RUN_INVOICE_CLASS_ALREADY_EXISTS = 'RUN_INVOICE_CLASS_ALREADY_EXISTS'
    UPLOADED_SUCCESSFULLY = 'UPLOADED_SUCCESSFULLY'
    RUN_INVOICE_CONTENT_DELETED = 'RUN_INVOICE_CONTENT_DELETED'
    RUN_INVOICE_CONTENT_UPDATED = 'RUN_INVOICE_CONTENT_UPDATED'
    UNAUTHORIZED_VIEW = 'UNAUTHORIZED_VIEW'
    UNAUTHORIZED_MOVE = 'UNAUTHORIZED_MOVE'
    UNAUTHORIZED_UPLOAD = 'UNAUTHORIZED_UPLOAD'
    CHANGE_CAN_UPLOAD_SUCCESSFUL = 'CHANGE_CAN_UPLOAD_SUCCESSFUL'
    CHANGE_PROPRIETOR_SUCCESSFUL = 'CHANGE_PROPRIETOR_SUCCESSFUL'
    CHANGE_INVOICE_CLASS_VISIBILITY_SUCCESSFUL = 'CHANGE_INVOICE_CLASS_VISIBILITY_SUCCESSFUL'
    RUN_INVOICE_CLASS_CREATED='RUN_INVOICE_CLASS_CREATED'
    PROCESS_RULE_STARTED='PROCESS_RULE_STARTED'
    FAIL_TO_START_PROCESS_RULE='FAIL_TO_START_PROCESS_RULE'
    RUN_PROCESS_NOT_FOUND='RUN_PROCESS_NOT_FOUND'
    RUN_PROCESS_IS_NOT_PONCTUAL='RUN_PROCESS_IS_NOT_PONCTUAL'
    NOTHIN_TO_MERGE='NOTHIN_TO_MERGE'
    FREQUENCY_OF_PROCESS_RULE_IS_PONTUAL='FREQUENCY_OF_PROCESS_RULE_IS_PONTUAL'
    RUN_PROCESS_MERGED='RUN_PROCESS_MERGED'
    CONNECTION_FAILED='CONNECTION_FAILED'
    TESTED_AND_CREATED_SUCCESSFULLY='TESTED_AND_CREATED_SUCCESSFULLY'
    NOTIFICATION_NOT_FOUND='NOTIFICATION_NOT_FOUND'
    NOTIFICATION_UPDATED_SUCCESSFULLY = 'NOTIFICATION_UPDATED_SUCCESSFULLY'
    NOTIFICATION_ALREADY_READ = 'NOTIFICATION_ALREADY_READ'
    NOTIFICATION_ERROR = 'NOTIFICATION_ERROR'
    NOTIFICATION_SUCCESSFUL = 'NOTIFICATION_SUCCESSFUL'
    POWEN_CONNECTION_URL_SUCCESSFULY_GENERATED = 'POWEN_CONNECTION_URL_SUCCESSFULY_GENERATED'
    ACCOUNT_SYNCHRONIZED_SUCCESSFULLY = 'ACCOUNT_SYNCHRONIZED_SUCCESSFULLY'
    BANK_ACCOUNT_NOT_FOUND = 'BANK_ACCOUNT_NOT_FOUND'
    BANK_ACCOUNT_CREATED_SUCCESSFULLY = 'BANK_ACCOUNT_CREATED_SUCCESSFULLY'
    BANK_CONNECTION_TITLE_ALREADY_EXISTS = 'BANK_CONNECTION_TITLE_ALREADY_EXISTS'
    INVOICE_CATEGORY_NOT_FOUND = 'INVOICE_CATEGORY_NOT_FOUND'

class EnumStatusResponse(Enum):
    SUCCESS = 'SUCCESS'
    FAILURE = 'FAILURE'
