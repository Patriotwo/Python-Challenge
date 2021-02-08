import os
import csv


csvpath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile) 


# Create a list to count the number of voters in voter ID row [0]
    voter_ID = []

# Create a list for candidate names
    candidate_list = []

# Create a list to count each of the candidate vote
    Khan_Vote = 0
    Correy_Vote = 0
    Li_Vote = 0
    OTooley_Vote = 0
    winning_candidate = []
    number_votes = 0
    
    


# Why is this action different from PyBank - row = next(csvreader)
    for row in csvreader:

# Count the number of votes
        number_votes += 1

# Return a list of candidate votes      
        if (row[2]) == ("Khan"):
            Khan_Vote += 1
        elif(row[2]) == ("Correy"):
            Correy_Vote += 1
        elif(row[2]) == ("Li"):
            Li_Vote += 1
        else:
             OTooley_Vote += 1

                
 # Calculate the percentage of each candidate votes
 #I need eac candidates individual total votes
 #This needs to be Total votes / "Khan" votes * 100
 #Total votes / "Correy" votes * 100 
 #Total votes / "Li" votes * 100 
 #Total votes / "O'Tooley" votes  * 100
 # take off the *100
      
        khan_percent = (Khan_Vote / number_votes)
        correy_percent = (Correy_Vote / number_votes)
        li_percent = (Li_Vote / number_votes)
        otooley_percent = (OTooley_Vote / number_votes)

#Calculte the winner    
    winner = max(Khan_Vote, Correy_Vote, Li_Vote, OTooley_Vote)
    if winner == Khan_Vote:
       winning_candidate = "Khan"
    elif winner == Correy_Vote:
        winning_candidate = "Correy"
    elif winner == Li_Vote:
        winning_candidate = "Li"
    else:
        winning_candidate = "O'Tooley"

    print(f'Election Results')
    print(f'-------------------------------------------')
    print(f'Total Votes: {number_votes}')
    print(f'Khan: {khan_percent:.3%} ({Khan_Vote})')
    print(f'Correy: {correy_percent:.3%} ({Correy_Vote})')
    print(f'Li: {li_percent:.3%} ({Li_Vote})')
    print(f"O'Tooley: {otooley_percent:.3%} ({OTooley_Vote})")
    print(f'-------------------------------------------')
    print(f'Winner: {winning_candidate}')
    print(f'-------------------------------------------')


    # Output files

    output_file = os.path.join('.', 'PyPoll', 'Resources', 'election_data_revised.text')

    with open(output_file, 'w',) as txtfile:


        txtfile.write(f'Election Results')
        txtfile.write(f'-------------------------------------------')
        txtfile.write(f'Total Votes: {number_votes}')
    
    
        txtfile.write(f'Khan: {khan_percent:.3%} ({Khan_Vote})')
        txtfile.write(f'Correy: {correy_percent:.3%} ({Correy_Vote})')
        txtfile.write(f'Li: {li_percent:.3%} ({Li_Vote})')
        txtfile.write(f"O'Tooley: {otooley_percent:.3%} ({OTooley_Vote})")
        txtfile.write(f'-------------------------------------------')
        txtfile.write(f'Winner: {winning_candidate}')
        txtfile.write(f'-------------------------------------------')
    
