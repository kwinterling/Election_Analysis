# The data we need to retrieve.
# 1. Total votes cast
# 2. List all candidates who received at least one vote
# 3. Percentage of votes for each candidate
# 4. Total votes for each candidate
# 5. Election winner based on popular vote

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

# Output file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a vote counter

total_votes = 0

# Candidate options

candidate_options = []

# Dictionary for candidate votes

candidate_votes = {}

# Winning candidate tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open and read election results

with open(file_to_load) as election_data:
    # TO DO: Analysis
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Count rows
    for row in file_reader:
        # increment counter
        total_votes += 1

        # Get the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match an existing candidate...
        if candidate_name not in candidate_options:
            # append to candidate_options list
            candidate_options.append(candidate_name)

            # begin tracking vote count
            candidate_votes[candidate_name] = 0
        
        # tally votes
        candidate_votes[candidate_name] += 1




print(total_votes)

# Print candidate list
print(candidate_options)

# Print vote tallies
print(candidate_votes)

# Determine the percentages of votes
# Iterate through candidates
for candidate_name in candidate_votes:
    # Retrieve vote count
    votes = candidate_votes[candidate_name]
    # calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # format percentage, see https://stackoverflow.com/questions/2389846/python-decimals-format#2390047
    formatted_percentage = '%.3g'%(vote_percentage)

    # add decimal if rounded to whole number
    if '.' not in formatted_percentage:
        formatted_percentage = formatted_percentage + ".0"

    # Print candidate name and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if votes is greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true, set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # set winning candidate to current candidate name
        winning_candidate = candidate_name


winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"-------------------------\n")

print(winning_candidate_summary)

