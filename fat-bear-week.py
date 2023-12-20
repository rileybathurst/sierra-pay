# this caluates the daily hours not weekly
import pandas as pd

sierra = pd.read_csv("Timesheets Report 11_27_2023-12_10_2023-2.csv", on_bad_lines='skip', skiprows=1)

# Convert the "Date" column to a datetime type
sierra["Date"] = pd.to_datetime(sierra["Date"])

# Find all the Sundays
sundays = sierra[sierra["Date"].dt.dayofweek == 6]

# Print the Sundays
print(sundays)

# ? this moght not work if no one works a sunday

