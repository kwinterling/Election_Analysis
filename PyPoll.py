# The data we need to retrieve.
# 1. Total votes cast
# 2. List all candidates who received at least one vote
# 3. Percentage of votes for each candidate
# 4. Total votes for each candidate
# 5. Election winner based on popular vote

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

# Open and read election results

with open(file_to_load) as election_data:
    # TO DO: Analysis
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

# Output file
file_to_save = os.path.join("analysis", "election_analysis.txt")


