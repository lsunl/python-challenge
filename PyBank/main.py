import os
import csv
import pandas as pd



csvpath = os.path.join('budget_data.csv')
data = pd.read_csv("budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    #Loop through each row
    #Total months = Add each row to an empty list and find the length of the list
    #Net profit = Add all the values of the profit/loss column
    months = 0
    net = 0
    dates = []
    for row in csvreader:
        shmoney = row[1]
        net += int(shmoney)
        dates.append(row[0])
        months += 1

    #The average of the changes in "Profit/Losses" over the entire period
    pl = data["Profit/Losses"]
    averagechange1 = []

    for x in range(0, len(pl)-1):
        averagechange1.append(pl[x+1] - pl[x])
    averagechange2 = sum(averagechange1) / len(averagechange1)
    averagechange3 = "{0:.2f}".format(averagechange2)

    #The greatest increase in profits (date and amount) over the entire period
    increase = max(averagechange1)

    #The greatest decrease in losses (date and amount) over the entire period
    decrease = min(averagechange1)

    #Find the index by adding 1 to get the right date
    maxdate = dates[(averagechange1.index(increase) +1)]
    mindate = dates[(averagechange1.index(decrease) +1)]

    #Summary of finances
    output = (
        "Financial Analysis \n----------------------------\n"
        f"Total Months: {months}\n"
        f"Total: $ {net}\n"
        f"Average Change: $ {averagechange3}\n"
        f"Greatest Increase in Profits: {maxdate} {increase}\n"
        f"Greatest Decrease in Profits: {mindate} {decrease} \n")
    print(output)


#create text file
file = open("PyBank.txt" , "w")
file.write(output)
file.close()
