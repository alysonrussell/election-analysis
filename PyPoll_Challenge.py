# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Declare a new list for Counties
county_options = []
# Declare an empty dictionary for County Votes
county_votes = {}
# Declare a new list for Candidate Options
candidate_options = []
# Declare an empty dictionary for Candidate Votes
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_county = ""
winning_count = 0
winning_percentage = 0
winning_candidate = ""
winning_candidate_count = 0
winning_candidate_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the county name from each row
        county_name = row[1]

        # If the county does not match any existing county...
        if county_name not in county_options:
            # Add it to the list of counties.
            county_options.append(county_name)
            # Begin tracking that county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's count.
        county_votes[county_name] += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
            f"County Votes:\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # Determine the percentage of votes for each county by looping through the counts.
        # Iterate through the county list
        for county in county_votes:
            # Retrieve vote count of a county.
            votes = county_votes[county]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            # Initialize variable for County Results
            county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print out each county's name, vote count, and percentage of votes to the terminal.
            print(county_results)
            # Save the candidate results to our text file.
            txt_file.write(county_results)

            # Determine winning vote count and county
            # Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning count = votes and winning percent = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # Set the winning_county equal to the candidate's name.
                winning_county = county

        # Print the winning county's results to the terminal.
        winning_county_summary = (
            f"-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n")
        print(winning_county_summary)

        # Save the winning county's name to the text file.
        txt_file.write(winning_county_summary)

        # Determine the percentage of votes for each candidate by looping through the counts.
        # Iterate through the candidate list
        for candidate in candidate_votes:
            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            # Initialize variable for Candidate Results
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print out each candidate's name, vote count, and percentage of votes to the terminal.
            print(candidate_results)
            # Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count.
            if (votes > winning_candidate_count) and (vote_percentage > winning_candidate_percentage):
                # If true then set winning count = votes and winning percent = vote_percentage
                winning_candidate_count = votes
                winning_candidate_percentage = vote_percentage
                # Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate

        # Print the winning candidates' results to the terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_candidate_count:,}\n"
            f"Winning Percentage: {winning_candidate_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)

        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)