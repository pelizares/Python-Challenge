import os
import csv
# path = "02-Homework/03-Python/Starter_Code/PyBank/Resources/budget_data.csv"

csvpath = os.path.join( "Resources", "budget_data.csv")

# total_months = 0
# Amount= 0
# average = 0
# max_change = 0
# min_change = 999999999999999999

# max_date = ""
# min_date = ""

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    #make lists
    number_month = []  
    profit_amount = []
    change_profit = []


    for row in csvreader:
        number_month.append(row[0])
        profit_amount.append(int(row[1]))
    for i in range (len(profit_amount)-1):
        change_profit.append(profit_amount[i+1]-profit_amount[i])


#Change in profit/losses
increase = max(change_profit)
decrease = min(change_profit)
#adding the months
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1
#calculating the average
avg_change = sum(change_profit)/len(change_profit)
avg_change = round(avg_change,2)
#increase/decrease
g_increase = number_month[month_increase]
g_decrease = number_month[month_decrease]


print ("Financial Analysis")
print ("---------------------------------------")
print (f"Total Months: {len(number_month)}")
print (f"Total: ${sum(profit_amount)}")
print(f"Average Change: ${avg_change}")
print (f"Greatest Increase in Profits: {g_increase} (${(str(increase))})")
print (f"Greatest Decrease in Profits: {g_decrease} (${(str(decrease))})")

output_pybank = os.path.join (".", "output_pybank.txt")
f = open(output_pybank,"w")
with open (output_pybank,"w") as f:

    f.write("Financial Analysis")
    f.write ("---------------------------------------")
    f.write (f"Total Months: {len(number_month)}")
    f.write (f"Total: ${sum(profit_amount)}")
    f.write(f"Average Change: ${avg_change}")
    f.write (f"Greatest Increase in Profits: {g_increase} (${(str(increase))})")
    f.write (f"Greatest Decrease in Profits: {g_decrease} (${(str(decrease))})")
