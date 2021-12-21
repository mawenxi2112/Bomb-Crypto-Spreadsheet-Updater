import pygsheets
import inquirer
import logging
import yaml
from prettytable import PrettyTable
from src.logger import logger, date_formatted, clear_console

stream = open("./config.yaml", 'r')
cfg = yaml.safe_load(stream)

# Table Variables
dailyProgressTableRange = cfg["daily_progress_table_range"]
claimTableRange = cfg["claim_table_range"]

bcoinPriceCell = cfg["stat_bcoin_curr_price_cell"]
bcoinWalletCell = cfg["stat_bcoin_wallet_cell"]
bcoinClaimedCell = cfg["stat_bcoin_claimed_cell"]
bcoinUnclaimedCell = cfg["stat_bcoin_unclaimed_cell"]
walletTotal = cfg["stat_wallet_total_cell"]
capitalCell = cfg["stat_capital_cell"]
roiPercentageCell = cfg["stat_roi_percentage_cell"]
roiDaysCell = cfg["stat_roi_days_cell"]
averageDailyCell = cfg["stat_average_daily_cell"]
netProfitCell = cfg["stat_net_profit_cell"]

# Authenticate client access to spreadsheet
googleConsole = pygsheets.authorize()

# Open spreadsheet and worksheet
spreadSheet = googleConsole.open('BCRYPTO')
workSheet = spreadSheet.sheet1


def add_daily_progress_entry():

    dailyprogresstable = workSheet.range(dailyProgressTableRange)
    for row in dailyprogresstable:

        if not row[0].value:

            date = date_formatted("%d/%m/%Y %I:%M%p")
            bcoin = input("enter current bcoin in chest: ")

            workSheet.update_value(row[0].label, date)
            workSheet.update_value(row[1].label, bcoin)

            logger("successfully added new entry for daily progress for " + date + " with " + bcoin + " bcoin", "green")
            return

    print("failed to find any empty rows to add new entry!")


def add_token_claim_entry():

    claimprogresstable = workSheet.range(claimTableRange)
    for row in claimprogresstable:

        if not row[0].value:
            date = date_formatted("%d/%m/%Y %I:%M%p")
            bcoin = input("enter bcoin claimed: ")
            actualbcoin = input("enter actual bcoin claimed: ")

            workSheet.update_value(row[0].label, date)
            workSheet.update_value(row[1].label, bcoin)
            workSheet.update_value(row[3].label, actualbcoin)

            logger("successfully added new entry for daily progress for " + date + " with " + bcoin + " bcoin and " + actualbcoin + " actual bcoin", "green")
            return

    print("failed to find any empty rsows in claim table to add new entry!")


def generate_daily_progress():
    table = PrettyTable()

    table.field_names = ["date", "chest", "gain (bcoin)", "gain (usd)"]

    dailySubstring = "date"
    dailyProgressSubstring ="daily"

    claimprogresstable = workSheet.range(dailyProgressTableRange)
    for row in claimprogresstable:

        if not dailySubstring in row[0].value.lower() and not dailyProgressSubstring in row[0].value.lower() and row[0].value:
            table.add_row([row[0].value, row[1].value, row[2].value, row[3].value])

    print(table.get_string() + "\n")


def generate_token_claim():
    pass


def generate_summary():
    table = PrettyTable()
    table.field_names = ["bcoin curr price", "total curr bcoin", "total wallet ($)", "roi (days)", "avg daily ($)", "net profit ($)"]
    table.add_row([workSheet.cell(bcoinPriceCell).value,
                   float(workSheet.cell(bcoinWalletCell).value) + float(workSheet.cell(bcoinClaimedCell).value) + float(workSheet.cell(bcoinUnclaimedCell).value),
                   workSheet.cell(walletTotal).value,
                   workSheet.cell(roiDaysCell).value,
                   workSheet.cell(averageDailyCell).value,
                   workSheet.cell(netProfitCell).value])

    print(table.get_string() + "\n")


def dump_to_csv():
    workSheet.export()
    logger("successfully dumped csv", "green")

while 1 > 0:

    choice = inquirer.list_input("select", choices=['add daily progress', 'add token claim', 'generate daily progress', 'generate token claim', 'generate summary', 'dump to csv', 'quit'])

    clear_console()

    if choice == "add daily progress":
        add_daily_progress_entry()
    elif choice == "add token claim":
        add_token_claim_entry()
    elif choice == "generate daily progress":
        generate_daily_progress()
    elif choice == "generate token claim":
        generate_token_claim()
    elif choice == "generate summary":
        generate_summary()
    elif choice == "dump to csv":
        dump_to_csv()
    elif choice == "quit":
        break

