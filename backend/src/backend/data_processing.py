#%%
import pandas as pd
from backend.constants import DATA_PATH

#read the solar.csv file into a pandas DataFrame
df = pd.read_csv(DATA_PATH / "solar.csv")

#fill missing values in the "Path Width (km)" and "Central Duration" columns with "00m00s" and "None" respectively
df["Path Width (km)"] = df["Path Width (km)"].fillna("None")
df["Central Duration"] = df["Central Duration"].fillna("00m00s")

#convert the "Central Duration" column from a string format (e.g., "00m00s") to seconds
def duration_to_seconds(val):
    if val == "00m00s" or val == "-": # Handle the case where the value is "00m00s" or "-" and return 0 seconds
        return 0
    minutes, seconds = val.replace("m", " ").replace("s", "").split() # Split the string into minutes and seconds by replacing "m" and "s" with spaces and splitting the resulting string
    return int(minutes) * 60 + int(seconds) # Convert the minutes to seconds and add the seconds to get the total duration in seconds

df["Central Duration (s)"] = df["Central Duration"].apply(duration_to_seconds) # Apply the duration_to_seconds function to the "Central Duration" column and create a new column "Central Duration (s)" with the converted values

#extract the year from the "Calendar Date" column and and remake to a number
df["Year"] = df["Calendar Date"].str.extract(r"(-?\d+)").astype(int) 

#%%
