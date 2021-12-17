import pygsheets
import numpy as np
import pandas as pd
from datetime import datetime

#Authenticate client access to spreadsheet
googleConsole = pygsheets.authorize()

#Open spreadsheet and worksheet
spreadSheet = googleConsole.open('BCRYPTO')
workSheet = spreadSheet.sheet1

#Table
dailyProgressTable = "A16"
claimProgressTable = "A16"

def add_daily_progress_entry():

    date = datetime.now().strftime("%d/%m/%Y %H:%M")
    bcoin = input("Enter current bcoin: ")

    workSheet.append_table([date, bcoin], dailyProgressTable, None, 'ROWS', true)
    print("New Daily Progress Entered for " + date + " with " + str(bcoin) + " bcoin")

testList = workSheet.range("A16:D60")
for i in testList:
    print(i)

