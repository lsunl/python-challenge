import os
import csv


csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #print(csv_header)

    #create empty dictionary, variables and lists
    results = {}

    totalvotes= 0
    candidates =[]
    votes = []
    percent = []

    #loop through each row to count the total number of votes
    #add candidates to the dictionary and iterate to count votes per name
    for row in csvreader:
        totalvotes += 1
        if row[2] not in results.keys():
            results[row[2]] = 1
        else:
            results[row[2]] += 1

    #loop through the dictionary to find percents
    #add candidates and percents to respective lists

    for key, value in results.items():
        candidates.append(key)
        percent.append("{0:.3f}".format(value/totalvotes*100))
        votes.append(value)

    #use the max function and find the index of the winner
    #the two list indexes correspond to each other
    winner = candidates[votes.index(max(votes))]

    #using this way because I couldn't figure out how to print all the results
    #of the dictionary without returning "dict_keys"
    output = (
        "Election Results\n----------------------------\n"
        f"Total Votes: {totalvotes}\n"
        "----------------------------\n"
        f"{candidates[0]}: {percent[0]} ({votes[0]}) \n"
        f"{candidates[1]}: {percent[1]} ({votes[1]}) \n"
        f"{candidates[2]}: {percent[2]} ({votes[2]}) \n"
        f"{candidates[3]}: {percent[3]} ({votes[3]}) \n"
        f"Winner: {winner}\n")


file = open("pypoll.txt", "w")

file.write(output)
file.close()
