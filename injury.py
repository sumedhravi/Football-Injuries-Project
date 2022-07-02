import pandas as pd
from data import data

# for item in data[400]:
#     print(item)

# likely_columns = [
#     "id",
#     "name",
#     "club",
#     "club_value",
#     "birthdate",
#     "height",
#     "country",
#     "role",
#     "kicks",
#     "transfers",
#     "injuries"
# ]

tuples = []
i=0
for t in open('Final-player.txt'):
    i=i+1
    if i == 2580:
        tuples.append(eval(t[1:-1]))
    else:
        tuples.append(eval(t[1:-2]))
df = pd.DataFrame(tuples)
df.columns = ["id", "name", "club","club_value","birth","weight","height","country","role","foot","transfers","injuries"]
number_of_players = df.shape[0]
print(df.columns)