from pydantic import BaseModel, Field
from typing import Literal, Optional, List

class ClaimState(BaseModel):
    claim_id: str
    claimant_name: str
    claim_amount: float
    incident_description: str
    documents: List[str] = Field(default_factory=list)
    status: Literal["pending", "validated", "fraud_review", "approved", "rejected", "escalated"] = "pending"
    validation_result: Optional[dict] = None
    fraud_score: Optional[float] = None
    decision_reason: Optional[str] = None
    next_action: Optional[str] = None