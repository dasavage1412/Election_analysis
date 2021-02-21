# The data we need to retrieve
# The total number of votes cast
# A complete list of candidatess who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won 
# The winner of the election based on the popular vote
import  csv
import os
file_to_load = 'election_results.csv'
with open(file_to_load) as election_data:
# To Do read and analyze here
    file_reader = csv.reader(election_data) 
    headers = next(file_reader)
    print(headers)







# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    # Adding couties to the election analysis doc   
    txt_file.write("Counties in the Election\n-----------------------------------\nArapahoe\nDenver\nJefferson")   


