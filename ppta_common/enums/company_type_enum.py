from enum import Enum


class CompanyType(str, Enum):
    CERTIFIED_ACCOUNTANT = 'CERTIFIED_ACCOUNTANT' #TODO: To be removed
    ESN = 'ESN' #TODO: To be removed
    FREELANCE = 'FREELANCE' #TODO: To be removed
    
    FINAL_CLIENT = 'FINAL_CLIENT' # Replaces FREELANCE
    ESN_SOURCING_RH = 'ESN_SOURCING_RH' # Replaces ESN
    CONSULTANT = 'CONSULTANT'
    COACH = 'COACH'