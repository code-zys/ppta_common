from enum import Enum


class ConnectionType(str,Enum):
    SMTP = 'SMTP'
    OAUTH = 'OAUTH2'
    DRIVE = 'DRIVE'