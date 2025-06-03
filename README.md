Install the poetry project

Get your Trades ("Transactions" fr) report from "https://www.kraken.com/c/account-settings/documents" with all fields as a csv file. 


Upload it in /dataset
Modify FILE_PATH_TRADES in main 

run python main.py


This is for all trades where actif was buy with fiat and sell to fiat (EUR/* and */EUR)

It's not working for actif to actif exchanges (crypto/crypto)