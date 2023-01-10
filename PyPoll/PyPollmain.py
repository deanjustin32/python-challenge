import os

import pandas as pd

csvfile = os.path.join("..", "PyPoll" , "election_data.csv")

election_data = pd.read_csv(csvfile)
 
df_election_data = pd.DataFrame(election_data)
 
percent_count = []
 
candidates = list(df_election_data["Candidate"].unique())
 
counts = list(df_election_data['Candidate'].value_counts())
 
total_votes = sum(counts)
 
x = 0
 
for candidate in candidates:
    percentage = counts[x]/total_votes
    percentage="{:.3%}".format(percentage)
    percent_count.append(percentage)
    x += 1
 
data = list(zip(candidates, percent_count, counts))
 
max_count = df_election_data['Candidate'].value_counts()
 
mostvotes = max_count.max()
 
df_data = pd.DataFrame(data)
 
winner = list(df_data.loc[df_data[2]== mostvotes,0])
 
electionresults =df_data.columns =["Candidate |", "Percent of Votes |", "Vote Count"]
 
electionresults = df_data.sort_values("Vote Count", ascending = False )
 
print("Election Results")
print(" -------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print(f"{electionresults}")
print(f" -------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

 
PyPollElectionResults = open("election_winner.txt","w")
 
PyPollElectionResults.write("Election Results\n")
PyPollElectionResults.write("----------------------------\n")
PyPollElectionResults.write(f"Total Votes: {total_votes}\n")
PyPollElectionResults.write(f"--------------------------\n")
PyPollElectionResults.write(f"{electionresults}\n")
PyPollElectionResults.write(f" -------------------------\n")
PyPollElectionResults.write(f"Winner: {winner}\n")
PyPollElectionResults.write(f"-------------------------")
 
PyPollElectionResults.close()
