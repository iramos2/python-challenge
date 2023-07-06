import os
import csv

#set the file path
csvpath = os.path.join("Resources", "budget_data.csv")

#reads and opens the file
with open(csvpath, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #initialize variables
    total_month = 0
    total_price = 0
    avg_price = 0
    net_total = 0
    month_diff = []
    prev_value = 0
    max_increase = 0
    min_loss = 0
    
    for row in csvreader:
        total_month = total_month + 1
        total_price = total_price + int(row[1])
        
        #calculates the difference from the current row to the previous row and stores it in a list
        #skips the first row during the first iteration
        if prev_value != 0:
            month_diff.append(int(row[1]) - int(prev_value))
        
        #stores the current row as a previous value
        prev_value = row[1]
            
        #collects the row with the greatest increase
        max_holder = int(row[1])
        if max_holder > max_increase:
            max_increase = max_holder
            max_row = row

        #collects the row with the greates decrease
        min_holder = int(row[1])
        if min_holder < min_loss:
            min_loss = min_holder
            min_row = row
    
    #calculate the sum of all the values in the month_diff list
    for num in month_diff:
        net_total += num
    #calculate the average change of the changes in profits/losses over time
    avg_price = net_total/(total_month-1)

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_month}")
    print(f"Net Total: ${total_price}")
    print(f"Average Change: ${avg_price: .2f}") #rounding 2 decimal places in the f-string was taken from stackoverflow
    print(f"Greatest Increase in Profits: {max_row[0]}", f" ${max_row[1]}")
    print(f"Greatest Decrease in Profits: {min_row[0]}", f" ${min_row[1]}")
    
    #export text file
    PyBook = os.path.join("analysis", "PyBook.txt")
    with open(PyBook, 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Financial Analysis"])
        writer.writerow(["----------------------------"])
        writer.writerow([f"Total Months: {total_month}"])
        writer.writerow([f"Net Total: ${total_price}"])
        writer.writerow([f"Average Change: ${avg_price: .2f}"]) #rounding 2 decimal places in the f-string was taken from stackoverflow
        writer.writerow([f"Greatest Increase in Profits: {max_row[0]}", f" ${max_row[1]}"])
        writer.writerow([f"Greatest Decrease in Profits: {min_row[0]}", f" ${min_row[1]}"])
