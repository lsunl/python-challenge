import os
import csv
import pandas as pd

data = pd.read_csv("budget_data.csv")



#The total number of months included in the dataset
months = data["Date"].count()
print(f"Total Months: {months}")


#The net total amount of "Profit/Losses" over the entire period
netprofit = data["Profit/Losses"].sum()
print(f"Total: {netprofit}")

#avg = data["Profit/Losses"].mean()
#print(avg)

#The average of the changes in "Profit/Losses" over the entire period
#How to find this using pandas?

pl = data["Profit/Losses"]
#date = data["Date"]
averagechange1 = []

for x in range(0, len(pl)-1):
    averagechange1.append(pl[x+1] - pl[x])

averagechange2 = sum(averagechange1) / len(averagechange1)
#averagechange2.to_numeric
print(f"Average  Change: $ {averagechange2}")



#The greatest increase in profits (date and amount) over the entire period
increase = max(averagechange1)
print(f"Greatest Increase in Profits: {increase}")

#The greatest decrease in losses (date and amount) over the entire period
decrease = min(averagechange1)
print(f"Greatest Decrease in Profits: {decrease}")


#Create a text file
"""
file = open("output.txt","w")

file.write("Financial Analysis" + "\n")
"""
