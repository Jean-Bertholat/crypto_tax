from pydantic import BaseModel

class Report(BaseModel):
    capital_gains: float = 0.0
    capital_losses: float = 0.0
    tax_due: float = 0.0 