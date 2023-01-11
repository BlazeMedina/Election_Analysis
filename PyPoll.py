# Add our dependencies.
import csv
import os

# Assign variable to load a file from a path.
file_to_load = os.path.join('Resources','election_results.csv')

# Assign variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Declare new list to hold candidate options
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}
# Winning Candidate and Wining Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # if the candidate name does not match any existing cadidate...
        if candidate_name not in candidate_options:
            # Add candidate name to candidate list
            candidate_options.append(candidate_name)

            # Track candidate vote count.
            candidate_votes[candidate_name]=0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # Calculate percentage
    vote_percentage = float(votes)/ float(total_votes)*100

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage
        winning_count=votes
        winning_percentage=vote_percentage
        # And, set the winning_candidate equal to the candidates name.
        winning_candidate=candidate_name

    # print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


#Print the winning summary
winning_candidate_summary = (
    f"-----------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n")
print(winning_candidate_summary)
