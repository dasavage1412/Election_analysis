# The data we need to retrieve
# The total number of votes cast
# A complete list of candidatess who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won 
# The winner of the election based on the popular vote
import  csv
import os
file_to_load = 'election_results.csv'
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Set total votes to 0
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
# To Do read and analyze here
    file_reader = csv.reader(election_data) 
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        
        candidate_name = row [2]

        if candidate_name not in candidate_options:
             candidate_options.append(candidate_name)
             candidate_votes[candidate_name] = 0  
        candidate_votes[candidate_name] += 1


with open(file_to_save, "w") as txt_file:
       
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
        
    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
            #format vote_percentage to one decimal  
            
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name  
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        winning_candidate_summary = (
            f"---------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------------\n"
            )
        #print(winning_candidate_summary) 
    for candidate in candidate_votes:
        txt_file.write(winning_candidate_summary)

