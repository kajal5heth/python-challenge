# Import modules for os and csv
import os
import csv

# Add the path for the csv file
bank_path = os.path.join('Resources','budget_data.csv')

total_months = 0
net_total_amount = 0
value = 0
net_changes = 0
profit_loss = []
dates = []


# Read the csv and convert to list of dictionaries
with open(bank_path) as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
    csv_header = next(csvreader)
    # Track changes
    first_row = next(csvreader)
    total_months += 1
    net_total_amount += int(first_row[1])
    value = int(first_row[1])

    # Going through rows after header         
    for first_row in csvreader:
        dates.append(first_row[0])
    
        # Calculate net changes
        net_changes = int(first_row[1])-value
        profit_loss.append(net_changes)
        value = int(first_row[1])
    
        # Total months
        total_months +=1
    
        # Net profit/loss amount
        net_total_amount = net_total_amount + int(first_row[1])
    
# Calculate greatest increase and decrease
greatest_inc = max(profit_loss)
greatest_index = profit_loss.index(greatest_inc)
greatest_date = dates[greatest_index]
    
greatest_dec = min(profit_loss)
dec_index = profit_loss.index(greatest_dec)
dec_date = dates[dec_index]

avg_change = sum(profit_loss)/len(profit_loss)

print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(net_total_amount)}")
print(f"Average Change: {str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_inc)})")
print(f"Greatest Decrease in Profits: {dec_date} (${str(greatest_dec)})")

# Export to a .txt file

output = open("Analysis/Analysis.txt", 'w')
analysis = (f"Financial Analysis\n"
         f"----------------------------\n"
         f"Total Months: {str(total_months)}\n"
         f"Total: ${str(net_total_amount)}\n"
         f"Average Change: ${str(round(avg_change,2))}\n"
         f"Greatest Increase in Profits: {greatest_date} (${str(greatest_inc)})\n"
         f"Greatest Decrease in Profits: {dec_date} (${str(greatest_dec)})\n")
output.write(analysis)