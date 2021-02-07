import os
import csv


csvpath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile) 


# Variables
    candidate = ["Khan", "O'Tooley", "Li", "Correy"]
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
           candidate_index = candidate.index(candidate_list)
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

    print(f'Election Results')
    print(f'-------------------------------------------')
    print(f'Total Votes: {total_votes}')
    for count in range(len(candidate_list)):
        print(f'{candidate_list[count]}: {percentage[count]}% ({candidate_vote_counter[count]}')
    print(f'-------------------------------------------')
    print(f'Winner: {winner}')
    print(f'--------------------------------------------')


    # Output files

    output_file = os.path.join('.', 'PyPoll', 'Resources', 'election_data_revised.text')

    with open(output_file, 'w',) as txtfile:


        txtfile.write(f'Election Results')
        txtfile.write(f'-------------------------------------------')
        txtfile.write(f'Total Votes: {total_votes}')
          for count in range(len(candidate_list)):
              txtfile.write(f'{candidate_list[count]}: {percentage[count]}% ({candidate_vote_counter[count]}')
        txtfile.write(f'-------------------------------------------')
        txtfile.write(f'Winner: {winner}')
        txtfile.write(f'--------------------------------------------')
    
