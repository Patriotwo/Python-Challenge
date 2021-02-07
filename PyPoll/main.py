import os
import csv


csvpath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile) 


# Variables
    candidate_list = ["Khan", "O'Tooley", "Li", "Correy"]
    candidate = []
    percentage = 0
    total_votes = 0
    candidate_vote_counter = Counter
    


# Why is this action different from PyBank - row = next(csvreader)
    for row in csvreader:
       
        total_votes += 1

# Return a list of candidate votes      
        candidate_list = (row[2])
        # step through candidate list
        if candidate in candidate_list
           candidate_index = candidate.index(candidate)
           candidate_vote_counter[candidate_index] = candidate_vote_counter[candidate_index] + 1
        else
           
 # Calculate the total number of votes each candidate won          
           candidate_list.append(candidate)
           candidate_vote_counter.append(1)

# Calculate percentage of votes for each candidate
           vote_tally = candidate_vote_counter[0]
           vote_tally_index = 0

    for count in range(len(candidate_list)):
        percentage = candidate_vote_counter[count]/total_votes*100
        total_percentage.append(percentage)
        if candidate_vote_counter[count] > vote_tally:
            vote_tally - candidate_vote_counter[count]
            print vote_tally
            vote_tally_index = count
    
    winner = candidate_list[vote_tally_index]
    




    
