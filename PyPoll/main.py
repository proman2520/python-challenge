import csv

with open("./PyPoll/Resources/election_data.csv", 'r') as file:
    election_data = csv.reader(file)

    #Code starts here?

    for row in election_data:
        #Do some things here
        print(row)