import os
import csv



csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    #Loop through each row
    #Total months = Add each row to an empty list and find the length of the list
    #Net profit = Add all the values of the profit/loss column
    months = 0
    net = 0
    dates = []
    money = []
    for row in csvreader:
        net += int(row[1])
        dates.append(row[0])
        money.append(row[1])
        months += 1

    #The average of the changes in "Profit/Losses" over the entire period
    averagechange1 = []

    for x in range(0, len(money)-1):
        averagechange1.append(int(money[x+1]) - int(money[x]))
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
