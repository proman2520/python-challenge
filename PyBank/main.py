import csv

with open("./PyBank/Resources/budget_data.csv", 'r') as file:
    budget_data = csv.reader(file)

    #Initial array and necessary variables
    budget_array = []
    header_row = []
    net_total = 0
    total_change = 0
    avg_change = 0
    initial_profit = 0
    max_profits = ["", 0]
    max_losses = ["", 0]

    c = 0

    #Turn the budget_array into a 2D array
    for row in budget_data:
        budget_array.append(row)

    #To store and remove the heading row
    header_row = [budget_array[0]]
    budget_array.pop(0)

    #The net total amount of "Profit/Losses" over the entire period
    for each in budget_array:
        net_total = net_total + int(budget_array[c][1])
        c += 1

    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    initial_profit = int(budget_array[0][1])
    c = 0
    for each in budget_array:
        if c == 0:
            total_change = int(budget_array[c][1]) - initial_profit
        else:
            total_change = total_change + (int(budget_array[c][1]) - int(budget_array[c-1][1]))
        c += 1

    avg_change = round(total_change / (len(budget_array) - 1), 2)

    #The greatest increase in profits (date and amount) over the entire period
    c = 0
    for each in budget_array:
        if (int(budget_array[c][1])-int(budget_array[c-1][1])) > int(max_profits[1]):
            max_profits[0] = budget_array[c][0]
            max_profits[1] = int(budget_array[c][1])-int(budget_array[c-1][1])
        c += 1

    #The greatest decrease in profits (date and amount) over the entire period
    c = 0
    for each in budget_array:
        if (int(budget_array[c][1])-int(budget_array[c-1][1])) < int(max_losses[1]):
            max_losses[0] = budget_array[c][0]
            max_losses[1] = int(budget_array[c][1])-int(budget_array[c-1][1])
        c += 1

    #RESULTS
    print("")
    print("Financial Analysis")
    print("--------------------------------------------------")
    print(f"Total months: {len(budget_array)}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${avg_change}") #WRONG ANSWER
    print(f"Greatest Increase in Profits: {max_profits[0]} (${max_profits[1]})")
    print(f"Greatest Decrease in Profits: {max_losses[0]} (${max_losses[1]})")

#In addition, your final script should both print the analysis to the terminal and export a text file with the results. (NO IDEA)
    