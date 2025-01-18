from enum import Enum

class EnumRole(str, Enum):
    OWNER = 'OWNER'
    MANAGER = 'MANAGER'
    EMPLOYEE = 'EMPLOYEE'
    ACCOUNTANT = 'ACCOUNTANT'