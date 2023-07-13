import csv

with open("./PyPoll/Resources/election_data.csv", 'r') as file:
    election_data = csv.reader(file)

    #Initialize variables
    election_array = []
    total_votes = 0
    Stockham_votes = 0
    DeGette_votes = 0
    Doane_votes = 0
    Stockham_share = 0
    DeGette_share = 0
    Doane_share = 0
    election_winner = ""

    c = 0

    #Turn the election_data into a 2D array
    for row in election_data:
        election_array.append(row)

    #To store and remove the heading row
    header_row = [election_array[0]]
    election_array.pop(0)

    #Log the total_votes
    total_votes = len(election_array)

    #The total number of votes each candidate won, c is reinitialized just in case, however redundant
    c = 0
    for each in election_array:
        if election_array[c][2] == "Charles Casper Stockham":
            Stockham_votes += 1
        elif election_array[c][2] == "Diana DeGette":
            DeGette_votes += 1
        elif election_array[c][2] == "Raymon Anthony Doane":
            Doane_votes += 1
        else:
            print("Did not vote")
        c += 1

    #Determine the vote percentages
    Stockham_share = round(((Stockham_votes / total_votes) * 100), 3)
    DeGette_share = round(((DeGette_votes / total_votes) * 100), 3)
    Doane_share = round(((Doane_votes / total_votes) * 100), 3)

    #Determine the winner of the election
    if Stockham_votes > DeGette_votes and Stockham_votes > Doane_votes:
        election_winner = "Charles Casper Stockham"
    elif DeGette_votes > Stockham_votes and DeGette_votes > Doane_votes:
        election_winner = "Diana DeGette"
    elif Doane_votes > Stockham_votes and Doane_votes > DeGette_votes:
        election_winner = "Raymon Anthony Doane"
    else:
        print("We have a tie!")

    #RESULTS
    print("")
    print("Election Results")
    print("------------------------------------")
    print(f"Total votes: {total_votes}")
    print("------------------------------------")
    print(f"Charles Casper Stockham: {Stockham_share}% ({Stockham_votes})")
    print(f"Diana DeGette: {DeGette_share}% ({DeGette_votes})")
    print(f"Raymon Anthony Doane: {Doane_share}% ({Doane_votes})")
    print("------------------------------------")
    print(f"Election winner: {election_winner.upper()}")
    print("------------------------------------")

#In addition, your final script should both print the analysis to the terminal and export a text file with the results. (NO IDEA)
    results = ["","Election Results","------------------------------------",\
               f"Total votes: {total_votes}","------------------------------------",\
               f"Charles Casper Stockham: {Stockham_share}% ({Stockham_votes})",\
                f"Diana DeGette: {DeGette_share}% ({DeGette_votes})"\
                f"Raymon Anthony Doane: {Doane_share}% ({Doane_votes})","------------------------------------",\
                f"Election winner: {election_winner.upper()}",\
                 "------------------------------------"]

    with open("./PyPoll/analysis/results.txt", 'w') as file:
        for line in results:
            file.write(line)
            file.write("\n")

#Code end, remember to update README.