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

# Track counties where people casted votes (my friend told me she lived somewhere with a low population)

counties_options = []

# Dictionary for candidate votes

candidate_votes = {}
candidate_percentages = {}
candidate_results = []

# Track county turnout

county_turnout = {}
county_results = []

# Winning candidate tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track highest turnout
highest_turnout_county = ""
highest_turnout_votes = 0
highest_turnout_percentage = 0

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

        # Get county name
        county_name = row[1]

        # Get the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match an existing candidate...
        if candidate_name not in candidate_options:
            # append to candidate_options list
            candidate_options.append(candidate_name)

            # begin tracking vote count
            candidate_votes[candidate_name] = 0
        
        # check if this is the first vote cast in the county
        if county_name not in counties_options:
            # append county name to counties list
            counties_options.append(county_name)

            # begin tracking county turnout
            county_turnout[county_name] = 0

        # tally votes
        candidate_votes[candidate_name] += 1
        # tally county turnout
        county_turnout[county_name] += 1




# print(total_votes)

# Print candidate list
# print(candidate_options)

# Print vote tallies
# print(candidate_votes)

# Determine the percentages of votes
# Iterate through candidates
for candidate_name in candidate_votes:
    # Retrieve vote count
    votes = candidate_votes[candidate_name]
    # calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # format percentage, see https://stackoverflow.com/questions/2389846/python-decimals-format#2390047
    # formatted_percentage = '%.3g'%(vote_percentage)

    # add decimal if rounded to whole number
    # if '.' not in formatted_percentage:
    #    formatted_percentage = formatted_percentage + ".0"
    

    # Print candidate name and percentage of votes
    candidate_results.append(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if votes is greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true, set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # set winning candidate to current candidate name
        winning_candidate = candidate_name


# Determine county results
for county_name in county_turnout:
    # get turnout
    turnout = county_turnout[county_name]
    # find turnout as percentage of total votes
    turnout_percentage = float(turnout) / float(total_votes) * 100

    # Store output string
    county_results.append(f"{county_name}: {turnout_percentage:.1f}% ({turnout:,})\n")

    # Determine highest county turnout, see candidate algorithm above
    if (turnout > highest_turnout_votes) and (turnout_percentage > highest_turnout_percentage):
        highest_turnout_votes = turnout
        highest_turnout_percentage = turnout_percentage
        highest_turnout_county = county_name


winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"-------------------------\n")

# build results string
election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")

# county turnout
for result in county_results:
    election_results = (
        f"{election_results}"
        f"{result}"
    )

# add highest turnout county
election_results = (
    f"{election_results}\n"
    f"-------------------------\n"
    f"Largest County Turnout: {highest_turnout_county}\n"
    f"-------------------------\n"
)

# add candidate results
for result in candidate_results:
    election_results = (
        f"{election_results}"
        f"{result}"
    )

# add election winner
election_results = (
    f"{election_results}"
    f"{winning_candidate_summary}"
)
print(election_results)

# Write results to file
with open(file_to_save, "w") as outfile:
    outfile.write(election_results)


