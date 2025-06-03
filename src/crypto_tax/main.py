import csv

from loaders.build_report import build_report
from loaders.Kraken_trades import load_kraken_transactions
from loaders.buid_portfolio import build_portfolio

FILE_PATH_TRADES="C:/Users/Jean/Desktop/crypto_tax/src/crypto_tax/dataset/trades all.csv"

def main():
    transactions = load_kraken_transactions(FILE_PATH_TRADES)
    print(f"Loaded {len(transactions)} transactions from Kraken.")

    portfolio = build_portfolio(transactions, pair="EUR")

    print("\nPortfolio Summary:")
    print("================")
    for asset in portfolio:
        print(f"\nAsset: {asset.name}     Total Quantity Left: {asset.total_quantity_left}")
        for entry in asset.stack_buy:
            print(f"  Quantity_buy: {entry['quantity']}, Price: {entry['price']}")
        for entry in asset.stack_sell:
            print(f"  Quantity_sell: {entry['quantity']}, Price: {entry['price']}")
    
    
    print("\nCapital Gains Report:")
    print("==================")
    report = build_report(portfolio, transactions)
    
    print(f"\nSummary:")
    print(f"Total Capital Gains: {report.capital_gains:.2f}€")
    print(f"Total Capital Losses: {report.capital_losses:.2f}€")
    print(f"Net Taxable Gain: {report.capital_gains - report.capital_losses:.2f}€")
    print(f"Estimated Tax Due (30%): {report.tax_due:.2f}€")

if __name__ == "__main__":
    main()