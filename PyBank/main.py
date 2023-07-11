import csv

with open("./PyBank/Resources/budget_data.csv", 'r') as file:
    budget_data = csv.reader(file)

    #Code starts here?

    for row in budget_data:
        #Do some things here
        print(row)