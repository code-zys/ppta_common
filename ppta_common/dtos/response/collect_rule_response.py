from pydantic import Field, BaseModel


from typing import Any, Dict, Optional

class CollectRuleResponse(BaseModel):
    id: str
    title: Optional[str]
    subject: Optional[str]
    collected_from: Optional[str]
    has_attachment: bool
    before: str
    after: str
    contain: Optional[str]
    connection: Dict[str, Any] = Field(..., description="Détails de la connexion")
    invoice_id: str
    last_connection_date: Optional[int]
    last_connection_status: Optional[str]
    created_at: Optional[int]