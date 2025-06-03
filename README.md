Install the poetry project

Get your Trades ("Transactions" fr) report from "https://www.kraken.com/c/account-settings/documents" with all fields as a csv file. 


Upload it in /dataset
Modify FILE_PATH_TRADES in main 

run python main.py

it returns:

    1. the transactions by crypto
    2. The logs of the FIFO computation process on sells
    3. a Summary:
        Total Capital Gains: 
        Total Capital Losses:
        Net Taxable Gain: 
        Estimated Tax Due (30%): 


This is for all trades where crypto was buy with fiat and sell to fiat (EUR/* and */EUR)
It's not working for crypto to crypto exchanges (crypto/crypto)