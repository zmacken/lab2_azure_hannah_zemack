import pandas as pd
from backend.constants import DATA_PATH

#read the solar.csv file into a pandas DataFrame
df = pd.read_csv(DATA_PATH / "solar.csv")

#fill missing values in the "Path Width (km)" and "Central Duration" columns with "None"
df["Path Width (km)"] = df["Path Width (km)"].fillna("None")
df["Central Duration"] = df["Central Duration"].fillna("None")

# #convert the "Central Duration" column from a string format (e.g., "00m00s") to seconds
# def duration_to_seconds(val):
#     if val == "00m00s" or val == "None" or pd.isna(val):
#         return 0
#     minutes, seconds = val.replace("m", " ").replace("s", "").split()
#     return int(minutes) * 60 + int(seconds)

# df["Central Duration (s)"] = df["Central Duration"].apply(duration_to_seconds)

# #extract the year from the "Calendar Date" column and and remake to a number
# df["Year"] = df["Calendar Date"].str.extract(r"(-?\d+)").astype(int) 

