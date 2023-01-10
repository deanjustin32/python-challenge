import os

import csv
 
budget_data = os.path.join ("..", "PyBank","budget_data.csv")
months = []
profit_loss = []
 
with open (budget_data) as csvfile:
    readcsv = csv.reader(csvfile, delimiter = ",")
 
    csv_header = next(csvfile)
     
    for row in readcsv:
        months.append(row[0])
        profit_loss.append(int(row[1]))
         
    month_count = len(months)
     
    x = 1
    y = 0
     
    average_change = (profit_loss[1]-profit_loss[0])
     
    change = []
     
    for month in range(month_count-1):
        average_change = (profit_loss[x] - profit_loss[y])
        change.append(int(average_change))
        
        x += 1
        y += 1
         
    averagemonthlychange = round(sum(change)/(month_count -1),2)
  
    minchange = min(change)

    maxchange = max(change)

    minchangeindex = change.index(minchange)

    maxchangeindex = change.index(maxchange)

    minchangemonth = months[minchangeindex + 1]

    maxchangemonth = months[maxchangeindex + 1]
   
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("                                      ")
print("Financial Analysis")
print("--------------------------------------")
print(f"Months: {len(months)}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Monthly Change: {averagemonthlychange}")
print(f"Greatest Increase in Profits: {maxchangemonth} (${maxchange})")
print(f"Greatest Decrease in Profits: {minchangemonth} (${minchange})")
print("                                      ")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("                                      ")

PyBank_FinacialData = open("Financial_Analysis.txt","w")

PyBank_FinacialData.write("                                         \n")
PyBank_FinacialData.write("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
PyBank_FinacialData.write("                                         \n")
PyBank_FinacialData.write("Financial Analysis\n")
PyBank_FinacialData.write("-----------------------------------------\n")
PyBank_FinacialData.write(f"Months: {len(months)}\n")
PyBank_FinacialData.write(f"Total: ${sum(profit_loss)}\n")
PyBank_FinacialData.write(f"Average Monthly Change: ${averagemonthlychange}\n")
PyBank_FinacialData.write(f"Greatest Increase in Profits: {maxchangemonth} (${maxchange})\n")
PyBank_FinacialData.write(f"Greatest Decrease in Profits: {minchangemonth} (${minchange})\n")
PyBank_FinacialData.write("                                         \n")
PyBank_FinacialData.write("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")