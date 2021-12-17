import pygsheets
import inquirer
import logging
from src.logger import logger, date_formatted

# Table Variables (Make into config)
dailyProgressTableRange = "A16:D60"
claimProgressTable = "F16:I58"

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
    pass

def generate_summary():
    pass

def dump_to_csv():
    pass

while 1 > 0:

    choice = inquirer.list_input("select", choices=['add daily progress', 'add token claim', 'generate summary', 'dump to csv', 'quit'])

    if choice == "add daily progress":
        add_daily_progress_entry()
    elif choice == "add token claim":
        add_token_claim_entry()
    elif choice == "generate summary":
        generate_summary()
    elif choice == "dump to csv":
        dump_to_csv()
    elif choice == "quit":
        break

