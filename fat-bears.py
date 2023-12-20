# this caluates the daily hours not weekly
import pandas as pd

with open('.env', 'r') as f:
    for line in f:
        if 'exceptions' in line:
            exceptions = line.strip()

print(f"The contents of the .gitignore file are: {exceptions}")

sierra = pd.read_csv("Timesheets Report 11_27_2023-12_10_2023-2.csv", on_bad_lines='skip', skiprows=1)

# Get the unique names
names = sierra["Name"].unique()

# Loop over each name
for name in names:
    # Filter the DataFrame for rows where the "Name" column is the current name
    entries = sierra[sierra["Name"] == name]

    # Group by date and sum the hours
    hours = entries.groupby("Date")["Hours"].sum()

    # Loop over the hours Series
    for date, total_hours in hours.items():
        # If the name is in the exceptions file, use 8 hours as the limit
        if name == exceptions:
            limit = 8
        else:
            limit = 10

        # If the total hours are more than the limit
        if total_hours > limit:
            # Calculate how much over the limit the person worked
            over = round(total_hours - limit, 2)

            # Print the date and how much over they were
            print(f"On {date}, {name} worked {over} hours over {limit} hours.")