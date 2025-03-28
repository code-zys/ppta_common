from enum import Enum


class ConnectionType(str, Enum):
    SMTP = 'SMTP'
    OAUTH2 = 'OAUTH2'
    OAUTH = 'OAUTH'
    DRIVE = 'DRIVE'
