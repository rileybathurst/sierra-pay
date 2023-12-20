# this caluates if someone worked more than 40 hours in a week
import pandas as pd

with open('.env', 'r') as f:
    for line in f:
        if 'exceptions' in line:
            exceptions = line.strip()

print(f"The contents of the .gitignore file are: {exceptions}")

sierra = pd.read_csv("Timesheets Report 11_27_2023-12_10_2023-2.csv", on_bad_lines='skip', skiprows=1)

# Convert the "Date" column to a datetime type
sierra["Date"] = pd.to_datetime(sierra["Date"])

# Get the earliest and latest dates
start_date = sierra["Date"].min()
end_date = sierra["Date"].max()

# Get the unique names
names = sierra["Name"].unique()

# Get the day of the week for the start date
start_day = start_date.day_name()

# Generate a sequence of the first 7 dates from the start date
first_7_days = pd.date_range(start=start_date, periods=7)

# Generate a sequence of all dates from the start date to the end date
all_dates = pd.date_range(start=start_date, end=end_date)

# weekly overtime hours
# Loop over each date in the sequence
for date in all_dates:
    # If the date is a Monday
    if date.day_name() == "Monday":
        # Generate a sequence of 7 days starting from the date
        week = pd.date_range(start=date, periods=7)

        # Loop over each name
        for name in names:
            # Filter the DataFrame for rows where the "Name" column is the current name
            entries = sierra[sierra["Name"] == name]

            # Filter for rows where the "Date" is in the week
            week_entries = entries[entries["Date"].isin(week)]

            # Sum the hours for the week
            total_hours = week_entries["Hours"].sum()
            
            weekly_overtime = 40

            # If the total hours are more than 40
            if total_hours > weekly_overtime:
                # Print the name, total hours, and week start date without the time
                print(f"{name} worked {total_hours} hours in the week starting {date.day_name()}, {date.strftime('%Y-%m-%d')}, which is more than {weekly_overtime} hours.")
                
            else:
                # Group by date and sum the hours
                hours = entries.groupby("Date")["Hours"].sum()

                # Loop over the hours Series
                for date, total_hours in hours.items():
                
                    # If the name is in the exceptions file, use 8 hours as the limit
                    if name == exceptions:
                        limit = 8
                    else:
                        limit = 10

                # If the total hours are more than 10
                if total_hours > 10:
                    total_hours = round(total_hours - limit, 2)
                    
                    # Print the date and total hours
                    print(f"{date.strftime('%Y-%m-%d')}, {name} worked {total_hours} more than {limit} hours.")
