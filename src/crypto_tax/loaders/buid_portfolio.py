from typing import List
from classes.Asset import Asset
from classes.Transaction import Transaction


def build_portfolio(transactions: List[Transaction], pair: str) -> List[Asset]:
    assets = {}

    for tx in transactions:
        if tx.type == "buy" and tx.pair.endswith(f"/{pair}"):
            asset_name = tx.pair.split("/")[0]
            if asset_name not in assets:
                assets[asset_name] = Asset(name=asset_name)
            assets[asset_name].stack_buy.append({"quantity": tx.volume, "price": tx.price})
        
        if tx.type == "sell" and tx.pair.endswith(f"/{pair}"):
            asset_name = tx.pair.split("/")[0]
            if asset_name not in assets:
                assets[asset_name] = Asset(name=asset_name)
            assets[asset_name].stack_sell.append({"quantity": tx.volume, "price": tx.price})

    return list(assets.values())
