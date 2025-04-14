from enum import Enum
    
class EnumFinancialLineType(str, Enum):
    PAYMENT = "PAYMENT"
    WITHDRAW = "WITHDRAW"
    CANCEL = "CANCEL"
    APP_FEE = "APP_FEE"