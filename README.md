# Bomb Crypto Spreadsheet Updater
 A script that is incorporated with my own spreadsheet to track my earnings for the P2E NFT game Bomb Crypto. I'm also using this as an opportunity to pick up more on Python. This script is basically using google sheets as a backend, but you can solely utilise the 
 
This script only works with my own spreadsheet which you can make a copy of from [here](https://docs.google.com/spreadsheets/d/1e2uB5x0Fo6P4a9riHr3zcsDlb8YDo5mlz0L-LLHQafM/edit?usp=sharing). But you can make your own adjustments within the config file to adjust to your own spreadsheet but generally the table design has to be similar to my spreadsheet in order for it to work.

**Note: All data has to be inputted by you, you DO NOT have to put in any wallet addresses or sign into any wallet.**
**If you ever stumble upon a spreadsheet or tool that requires you to login with any wallet, it is more than likely a SCAM!**

## **Features**
- Add daily progress entry
- Add token claim entry
- Generate a table for daily progress
- Generate a table for token claims
- Generate a summary table which shows useful statistics such as bcoin price, total held bcoins, wallet worth, roi (days), roi (%), avg daily profit, net profit
- Dump spreadsheet into a local .csv file

## **How to use spreadsheet**

If you would like to only make a copy and use the spreadsheet, here's how to use it.
Most of the cells are filled with formulas and you only have to edit these few cells.

**Asset Table**
- BUSD (Your wallet USD/BUSD amount)
- BNB (Your wallet BNB amount)
- BCOIN Wallet (Your wallet BCOIN amount)

**Daily Progress Table**
- Date (Date of when you checked your bcoin amount)
- Chest (The amount of bcoin in your chest)

**Claim Table**
- Date (Date of when you claimed your tokens)
- Amount (Raw amount of tokens deducted from your chest in-game)
- Actual (Actual amount of tokens you received after fees)

## **How to use the script**

You will need your own client_secret.json file that is generated and downloaded from google's api, you can learn how to retrieve it [here](https://www.iperiusbackup.net/en/how-to-enable-google-drive-api-and-get-client-credentials/). Once you have it generated, you need to rename it to "client_secret" and put it in the same folder as the script.

Download and install python 3.9.9 and make sure to tick "install to PATH"

Run the following commands in terminal

```
pip install -r requirements.txt
```

```
python main.py
```

## **Screenshots**
