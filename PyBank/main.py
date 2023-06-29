# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

import os
import csv

#set the file path
csvpath = os.path.join(".." , "Resources", "budget_data.csv")

#open and read the file
with open(csvpath, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvpath, delimiter=",")
