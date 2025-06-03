from pydantic import BaseModel


class Asset(BaseModel):
    name: str
    stack_buy: list[dict] = []
    stack_sell: list[dict] = []
    
    @property
    def total_quantity_left(self) -> float:
        """
        Returns the total quantity of the asset currently in the stack.
        """
        return sum(item["quantity"] for item in self.stack_buy) - sum(item["quantity"] for item in self.stack_sell)

    @property
    def total_quantity_buy(self) -> float:
        """
        Returns the total quantity of the asset currently in the stack.
        """
        return sum(item["quantity"] for item in self.stack_buy) 
    
    @property
    def total_quantity_sell(self) -> float:
        """
        Returns the total quantity of the asset currently in the stack.
        """
        return sum(item["quantity"] for item in self.stack_sell)
