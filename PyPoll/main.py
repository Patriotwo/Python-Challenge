import os
import csv


csvpath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile) 


# Variables
    candidate = []
    candidate_list = []
    count = 0
    percentage = []
    number_votes = 0
    candidate_vote_counter = []
    x = {"Khan", "Correy", "Li", "O'Tooley"}


# Why is this action different from PyBank - row = next(csvreader)
    for row in csvreader:
       
        number_votes += 1

# Return a list of candidate votes      
        candidate_list.append(row[2])

        # step through candidate list
    for x in set(candidate_list):
        candidate.append(x)   
        
 # Calculate the total number of votes each candidate won  
 """ I need eac candidates individual total votes
 This needs to be Total votes / "Khan" votes * 100
 Total votes / "Correy" votes * 100 
 Total votes / "Li" votes * 100 
 Total votes / "O'Tooley"  * 100"""     
        y = candidate_list.count(x)
        candidate_vote_counter.append(y)

# Calculate the percentage of the votes for each candidate 
        z = (y/number_votes)*100
        percentage.append(z)
    
    winning_count = max(candidate_vote_counter)
    winner = candidate.index(winning_count)

    print(f'Election Results')
    print(f'-------------------------------------------')
    print(f'Total Votes: {number_votes}')
    
    for count in range(len(candidate_list)):
        print(f'{candidate_list[x]}: {percentage[z]}% ({candidate_vote_counter[y]})')
        print(f'-------------------------------------------')
        print(f'Winner: {winner}')
        print(f'-------------------------------------------')


    # Output files

    output_file = os.path.join('.', 'PyPoll', 'Resources', 'election_data_revised.text')

    with open(output_file, 'w',) as txtfile:


        txtfile.write(f'Election Results')
        txtfile.write(f'-------------------------------------------')
        txtfile.write(f'Total Votes: {number_votes}')
    
    for count in range(len(candidate_list)):
        txtfile.write(f'{candidate_list[x]}: {percentage[z]}% ({candidate_vote_counter[y]})')
        txtfile.write(f'-------------------------------------------')
        txtfile.write(f'Winner: {winner}')
        txtfile.write(f'-------------------------------------------')
    
