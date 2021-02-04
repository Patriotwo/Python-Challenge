import os
import csv

# read the CSV file 

PyBankcsv = os.path.join('PyBank','Resources','budget_data.csv')

# names to store dataset values

total_months = []
date = []
total_monthly_change = []
profit = []
pl_change = []

#Store Values
counter = 0
pl_total = 0
begin_profit = 0
monthly_change = 0
total_pl_change = 0

with open(PyBankcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader) 
    
    for row in csvreader:

# Count the total number of months
      date.append(row[0])
      counter = counter + 1 

# Calculate the total profit and loss
      profit.append(row[1])
      pl_total = pl_total + int(row[1])
        
# Calculate the changes in in profit/loss and find the average       
      pl_change = int(row[1])
      monthly_change = pl_change - begin_profit
      
      total_monthly_change.append(monthly_change)

      total_pl_change = total_pl_change + monthly_change
      begin_profit = pl_change

      pl_average = (total_pl_change/counter)

  #Greatest increase in profits (date and amount)    
      highest_pl = max(total_monthly_change)
      highest_date = date[total_monthly_change.index(highest_pl)]

      lowest_pl = min(total_monthly_change) 
      lowest_date = date[total_monthly_change.index(highest_pl)]
      
print(f"Financial Analysis")
print(f"-------------------------------------------")
print(f"Total Months: " + str(counter))
print(f"Total Profit/Loss: " + "$" + str(pl_total))
print(f"Average Change: " + "$" + str(pl_average))
print(monthly_change)