import os
import csv

csvpath = os.path.join( "Resources", "election_data.csv")

#dictionary
candidates = {}

#total votes
votes = 0

most_votes = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #loop through data
    for row in csvreader:
        votes += 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votes))
print("-------------------------")



for key, value in candidates.items():
    percent = value/votes
    print(key + ": " + "{:.3%}".format(percent) + "  (" + str(value) + ")")

print("-------------------------")

winner = max(candidates, key=candidates.get)   

print(f"Winner: {winner}")

print("-------------------------")



output_pypoll = os.path.join (".", "output_pypoll.txt")

with open (output_pypoll,"w") as f:

    f.write("Election Results")
    f.write("-------------------------")
    f.write("Total Votes: " + str(votes))
    f.write("-------------------------")
    f.write(key + ": " + "{:.3%}".format(percent) + "  (" + str(value) + ")")
    f.write("-------------------------")
    f.write(f"Winner: {winner}")
    f.write("-------------------------")







#         candidate_name = row[0]
#         votes = votes +1

#     if candidate_name in candidates:
#         candidates[candidate_name] = candidates[candidate_name] +1
#     else:
#         candidates[candidate_name] = 1


# for key, value in candidates.items():
#     if value > most_votes:
#         winner_name = key
#         most_votes = value


# print("Election Results")
# print("-------------------------------")
# print("Total Votes: " + str(candidates))
# print("-------------------------------")
# #print (f"{key} + ": " + {(str(value))}")

# print (str(candidates) + str(candidate_name))

# print(key + ": " + str(value))
# print (most_votes + " " + str(most_votes))
# print("\nMost Animal:")
