import os
import csv

#Thanks to Joseph Yon "Big1bluey" for the references and guidance of his code
# read the CSV file 

PyBankcsv = os.path.join('PyBank','Resources','budget_data.csv')


with open(PyBankcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
# names to store dataset values
    profit = []
    month_collect = []
    pl_change = []
    monthly_change = []
    month_count = []
    
#Store Values
    previous_row = 0
    net_total = 0
    total_months = 0
    total_profit = 0
    highest_pl = 0
    lowest_pl = 0
    
# This will start the csv reader on the 2nd row



    for row in csvreader:





# Count the total number of months
      
      total_months += 1 
      
# Calculate the total profit and loss

      net_total += int(row[1])
      
# Calculate the monthly changes in profit/loss over the entire dataset 
# Thanks to Joseph Yon "Bigbluey".  I struggled for 3-days with my solution 
      
      pl_change = int(row[1]) - previous_row
      monthly_change.append(pl_change)
      previous_row = int(row[1])
      month_count.append(row[0])
     


# find the average     
      
      total_month_change =  sum(monthly_change) - monthly_change[0]
      value_monthly_change = len(monthly_change) - 1
      
      average_change = total_month_change / 85
      # value_monthly_change = 85
      # toatal_average_change = (-196785)
      # using the names in the equation returns a Zero Division Error
      


  #Greatest increase in profits (date and amount)  Thanks to BigBluey  
      if int(row[1]) > highest_pl:        
         highest_pl = int(row[1])
         highest_date = row[0]
         greatest_increase = max(monthly_change)

      if int(row[1]) < lowest_pl:      
         lowest_pl = int(row[1])
         lowest_date = row[0]
         greatest_decrease = min(monthly_change)

print(f"Financial Analysis")
print(f"-------------------------------------------")
print(f"Total Months: " + str(total_months))
print(f"Total Profit/Loss: " + "$" + str(net_total))
print(f"Average Change: " + "$" + str(average_change))
print(f"Greatest Increase in Profits:, {str(highest_date)}, (${greatest_increase})")
print(f"Greatest Decrease in Profits:, {str(lowest_date)},  (${greatest_decrease})")


# export the results 
output_file = os.path.join('PyBank','Resources','budget_data.text')
with open(output_file, 'w',) as txtfile:

    txtfile.write(f"Financial Analysis")
    txtfile.write(f"-------------------------------------------")
    txtfile.write(f"Total Months: " + str(total_months))
    txtfile.write(f"Total Profit/Loss: " + "$" + str(net_total))
    txtfile.write(f"Average Change: " + "$" + str(average_change))
    txtfile.write(f"Greatest Increase in Profits:, {str(highest_date)}, (${greatest_increase})")
    txtfile.write(f"Greatest Decrease in Profits:, {str(lowest_date)},  (${greatest_decrease})")   