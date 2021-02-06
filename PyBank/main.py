import os
import csv


#Thanks to Joseph Yon "Big1bluey" for the references and guidance of his code
# read the CSV file 

PyBankcsv = os.path.join('PyBank','Resources','budget_data.csv')

# names to store dataset values

date = []
profit = []
month_collect = []
pl_change = []
net_total_pl = []
month_count = []
#Store Values
total_months = 0
total_profit = 0
row_count = -1
total_pl_change = 0


with open(PyBankcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader) 
    
    for row in csvreader:

# Count the total number of months
      date.append(row[0])
      total_months += 1 

# Calculate the total profit and loss

      total_profit += int(row[1])
      
# Calculate the monthly changes in in profit/loss      

      monthly_change = int(row[1]) - row_count

      month_collect.append(monthly_change)

      sum_pl = sum(month_collect)

      
      row_count = int(row[1])
      
      month_count.append(row[0])

# find the average     
      
      average_change = round(sum_pl)/(total_months) 


  #Greatest increase in profits (date and amount)    
      highest_pl = max(month_collect)
      highest_date = max(date)
      lowest_pl = min(month_collect)
      lowest_date = min(date)

       
      
      
print(f"Financial Analysis")
print(f"-------------------------------------------")
print(f"Total Months: " + str(total_months))
print(f"Total Profit/Loss: " + "$" + str(total_profit))
print(f"Average Change: " + "$" + str(average_change))
print(f"Greatest Increase in Profits:, {str(highest_date)}, (${highest_pl})")
print(f"Greatest Decrease in Profits:, {str(lowest_date)},  (${lowest_pl})")


# export the results 
output_file = os.path.join('PyBank','Resources','budget_data.text')
with open(output_file, 'w',) as txtfile:

    txtfile.write(f"Financial Analysis")
    txtfile.write(f"-------------------------------------------")
    txtfile.write(f"Total Months: " + str(total_months))
    txtfile.write(f"Total Profit/Loss: " + "$" + str(total_profit))
    txtfile.write(f"Average Change: " + "$" + str(average_change))
    txtfile.write(f"Greatest Increase in Profits:, {str(highest_date)}, (${highest_pl})")
    txtfile.write(f"Greatest Decrease in Profits:, {str(lowest_date)},  (${lowest_pl})")   