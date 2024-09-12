from enum import Enum

class EnumSecurityType(str, Enum):
    SSL = 'SSL'
    TLS = 'TLS'
    NONE = 'None'