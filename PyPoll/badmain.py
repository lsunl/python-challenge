import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #print(csv_header)

    votes= 0
    candidates = []
    khan = 0
    correy = 0
    li = 0
    ot = 0
    for row in csvreader:
        votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == "Khan":
            khan += 1
        if row[2] == "Correy":
            correy += 1
        if row[2] == "Li":
            li += 1
        if row[2] == "O'Tooley":
            ot +=1

    finals = [khan, correy, li, ot]

    winner = finals[finals.index(max(finals))]

    kp ="{0:.3f}".format(khan/votes * 100)
    lp = "{0:.3f}".format(li/votes * 100)
    cp = "{0:.3f}".format(correy/votes * 100)
    op = "{0:.3f}".format(ot/votes * 100)

    #Summary
    output = (
        "Election Results\n----------------------------\n"
        f"Total Votes: {votes}\n"
        "----------------------------\n"
        f"Khan: {kp}% ({khan}) \n"
        f"Correy: {cp}% ({correy}) \n"
        f"Li: {lp}% ({li}) \n"
        f"O'Tooley: {op}% ({ot}) \n"
        "----------------------------\n"
        f"Winner: {winner} \n")
    print(output)
