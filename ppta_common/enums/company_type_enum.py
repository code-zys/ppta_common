from enum import Enum


class CompanyType(str, Enum):
    CERTIFIED_ACCOUNTANT = 'CERTIFIED_ACCOUNTANT'
    ESN = 'ESN'
    FREELANCE = 'FREELANCE'
    FINAL_CLIENT = 'FINAL_CLIENT'