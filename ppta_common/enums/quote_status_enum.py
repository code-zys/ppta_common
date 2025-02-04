from enum import Enum


class EnumQuoteStatus(str, Enum):
    DRAFT = "DRAFT"       # Brouillon (modifiable et supprimable)
    SEND = "SEND"         # Envoyé au client (non modifiable, non supprimable)
    ACCEPTED = "ACCEPTED" # Accepté (non modifiable, non supprimable)
    DENIED = "DENIED" 
    INVALID_QUOTE_STATUS = "INVALID_QUOTE_STATUS"