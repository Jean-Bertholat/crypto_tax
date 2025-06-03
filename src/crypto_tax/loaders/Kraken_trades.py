import os
from typing import List
from classes.Transaction import Transaction_Kraken
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime


def load_kraken_transactions(file_path) -> List[Transaction_Kraken]:
    """
    Load Kraken transactions from a CSV file specified in environment variables
    Returns a list of Transaction_Kraken objects
    """
    
    if not file_path:
        raise ValueError("KRAKEN_CSV_PATH not found in environment variables")
    
    # Read CSV file
    df = pd.read_csv(file_path)
    
    transactions = []
    for _, row in df.iterrows():
        transaction = Transaction_Kraken(
            txid=str(row['txid']),
            pair=str(row['pair']),
            type=str(row['type']),
            price=float(row['price']),
            cost=float(row['cost']),
            volume=float(row['vol']),
            fee=float(row['fee'])
        )
        transactions.append(transaction)
    
    return transactions