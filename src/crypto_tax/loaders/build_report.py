from typing import List
from classes.Asset import Asset
from classes.Report import Report


def build_report(portfolio: List[Asset], transactions) -> Report:
    """
    Build a report from the given transactions using FIFO method.
    
    Args:
        portfolio (List[Asset]): List of assets to include in the report.
        transactions (List[Transaction]): List of transactions (not used currently).
        
    Returns:
        Report: A report containing capital gains and losses.
    """
    
    report = Report()
    
    for asset in portfolio:
        # Créer une copie modifiable des achats pour cet actif
        remaining_buys = []
        for buy in asset.stack_buy:
            remaining_buys.append({
                'quantity': buy['quantity'],
                'price': buy['price'],
                'original_quantity': buy['quantity']  # Garder une trace de la quantité originale pour le reporting
            })
        
        print("----------------------------------------")
        print(f"\nProcessing {asset.name} sales:")
        
        for sell in asset.stack_sell:
            sell_qty = sell['quantity']
            sell_price = sell['price']
            qty_needed = sell_qty
            total_sell_revenue = 0
            total_buy_cost = 0
            
            print(f"\nSell transaction: {sell_qty} units at {sell_price}€")
            print("Breaking down this sale into matching buys:")
            
            i = 0
            while qty_needed > 0 and i < len(remaining_buys):
                buy = remaining_buys[i]
                available_qty = buy['quantity']
                
                if available_qty <= 0:
                    i += 1
                    continue
                
                used_amount = min(available_qty, qty_needed)
                buy_price = buy['price']
                
                # Calculate gain/loss for this portion
                buy_cost = used_amount * buy_price
                sell_revenue = used_amount * sell_price
                gain_loss = sell_revenue - buy_cost
                
                total_sell_revenue += sell_revenue
                total_buy_cost += buy_cost
                
                if gain_loss > 0:
                    report.capital_gains += gain_loss
                else:
                    report.capital_losses += abs(gain_loss)
                
                # Update remaining quantity
                buy['quantity'] -= used_amount
                qty_needed -= used_amount
                
                print(f"\n  Part {i + 1} of sale:")
                print(f"    Using {used_amount} units from buy @ {buy_price}€")
                print(f"    Buy cost for this part: {buy_cost:.2f}€")
                print(f"    Sell revenue for this part: {sell_revenue:.2f}€")
                print(f"    Gain/Loss for this part: {gain_loss:.2f}€")
                print(f"    Remaining in this buy: {buy['quantity']}")
                print(f"    Still need to match: {qty_needed} units")
                
                i += 1
            
            # Afficher le résumé de la vente complète
            total_gain_loss = total_sell_revenue - total_buy_cost
            print(f"\n  Summary for this sell transaction:")
            print(f"    Total Buy Cost: {total_buy_cost:.2f}€")
            print(f"    Total Sell Revenue: {total_sell_revenue:.2f}€")
            print(f"    Total Gain/Loss: {total_gain_loss:.2f}€")
            
            if qty_needed > 0:
                print(f"\n  Warning: Not enough buy orders to cover sell of {sell_qty} {asset.name}")
                print(f"  Missing: {qty_needed} units")
            
            # Display remaining buy quantities after this sell
            print("\nRemaining buy orders:")
            for buy in remaining_buys:
                print(f"  {buy['quantity']}/{buy['original_quantity']} units @ {buy['price']}€")
            print("----------------------------------------")
    
    # Calculate tax due (example rate of 30%)
    report.tax_due = report.capital_gains * 0.30
    
    return report


