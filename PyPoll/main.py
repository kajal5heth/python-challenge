# Import modules for os and csv
import os
import csv

# Add the path for the csv file
vote_path = os.path.join('Resources','election_data.csv')

# Variables
candidates = []
vote_count = []
percent_votes = []
tot_votes = 0

# Read the file and get the data
with open(vote_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Going through rows after header         
    for first_row in csvreader:
        tot_votes += 1

        if first_row[2] not in candidates:
            candidates.append(first_row[2])
            index = candidates.index(first_row[2])
            vote_count.append(1)
            
        else:
            index = candidates.index(first_row[2])
            vote_count[index] += 1
                    
    for votes in vote_count:
        percentage = (votes/tot_votes) * 100
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Finding the winning candidate
    win_candidate = max(vote_count)
    index = vote_count.index(win_candidate)
    winner = candidates[index]

# Print the results    
print("Election Results")
print("-----------------------------------------") 
print(f"Total Votes: {str(tot_votes)}")
print("-----------------------------------------")
for i in range (len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(vote_count[i])})")
print("-----------------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------------")

# Exporting the results to .txt

output = open("Analysis/Analysis.txt", 'w')

analysis = (f"Election Results\n"
        f"-----------------------------------------\n"
        f"Total Votes: {str(tot_votes)}\n"
        f"-----------------------------------------\n")
output.write(analysis)

for i in range (len(candidates)):
    output.write((f"{candidates[i]}: {str(percent_votes[i])} ({str(vote_count[i])})\n"))
output.write(f"-----------------------------------\n"   
    f"Winner: {winner}\n"
    f"-----------------------------------------\n")

