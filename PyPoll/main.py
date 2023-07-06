# The total number of votes cast: Total Votes: 369711
# A complete list of candidates who received votes
    # Charles Casper Stockham: 23.049% (85213)
    # Diana DeGette: 73.812% (272892)
    # Raymon Anthony Doane: 3.139% (11606)
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

import os
import csv

#set the file path
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #initialize varialbes
    total_votes = 0
    candidates = {}
    winner = ""
    
    for row in csvreader:
        total_votes = total_votes + 1
        
        #add the candidate to the dictionary and totals the vote count
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
            
    winner = max(candidates, key=candidates.get)
    
    #calculates the percent votes
    percent_votes = {
        "Charles Casper Stockham": (candidates["Charles Casper Stockham"]/total_votes) * 100,
        "Diana DeGette": (candidates["Diana DeGette"]/total_votes) * 100,
        "Raymon Anthony Doane": (candidates["Raymon Anthony Doane"]/total_votes) * 100
    }

    #round the precent votes
    percent_votes_C = round(percent_votes["Charles Casper Stockham"], 2)
    percent_votes_D = round(percent_votes["Diana DeGette"], 2)
    percent_votes_R = round(percent_votes["Raymon Anthony Doane"], 2)
    
    PyPoll = os.path.join("analysis", "PyPoll.txt")
    with open(PyPoll, 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Election Results"])
        writer.writerow(["-------------------------"])
        writer.writerow([f"Total Votes: {total_votes}"])
        writer.writerow(["-------------------------"])
        writer.writerow([f"Charles Casper Stockham: {percent_votes_C}% ({candidates['Charles Casper Stockham']})"])
        writer.writerow([f"Diana DeGette:  {percent_votes_D}% ({candidates['Diana DeGette']})"])
        writer.writerow([f"Raymon Anthony Doane: {percent_votes_R}% ({candidates['Raymon Anthony Doane']})"])
        writer.writerow(["-------------------------"])
        writer.writerow([f"Winner: {winner}"])
        writer.writerow(["-------------------------"])