from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class Transaction(BaseModel):
    txid: str
    
class Transaction_Kraken(Transaction, BaseModel):
    pair: str
    type: str
    price: float
    cost: float
    volume: float
    fee: float