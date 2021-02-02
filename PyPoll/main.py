import os
import csv

csvpath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile) 
    # Why is this action different from PyBank - row = next(csvreader)
    for row in csvreader:
    
        print(row)
