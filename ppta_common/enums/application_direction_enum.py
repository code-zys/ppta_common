from enum import Enum

class EnumApplicationDirection(str, Enum):
    FROM_MEMBER_TO_COMPANY = 'FROM_MEMBER_TO_COMPANY'
    FROM_COMPANY_TO_MEMBER = 'FROM_COMPANY_TO_MEMBER'