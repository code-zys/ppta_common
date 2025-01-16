from pydantic import BaseModel

class InvoiceReconciliationDTO(BaseModel):
    transaction_id: str
    percentage: float
    date: int

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
        "from_attributes": True,
        "arbitrary_types_allowed": True
    }
