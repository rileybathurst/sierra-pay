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

if start_date.day_name() == "Monday":
    print("The first day is a Monday.")
    
    # Generate a sequence of dates from the start date to the end date with a frequency of 7 days
    weeks = pd.date_range(start=start_date, end=end_date, freq='7D')

    for name in names:
        # Filter the DataFrame for rows where the "Name" column is the current name
        entries = sierra[sierra["Name"] == name]

        # Loop over each date in the sequence
        for start_of_week in weeks:
            # Generate a sequence of 7 days starting from the date
            week = pd.date_range(start=start_of_week, periods=7)

            # Initialize a flag for each week
            printed_week = {start_of_week: False for start_of_week in weeks}
            # print(week)
            
            for days in week:
                # print(days.day_name())

                # Filter for rows where the "Date" is in the week
                week_entries = entries[entries["Date"].isin(week)]

                # Sum the hours for the week
                total_hours = week_entries["Hours"].sum()
                
                weekly_overtime = 40

                # Inside the loop
                for start_of_week in weeks:
                    # Rest of the code...

                    # If the total hours are more than 40 and the statement has not been printed for this week
                    if total_hours > weekly_overtime and not printed_week[start_of_week]:
                        # Print the statement
                        print (f"In the week starting {start_of_week.day_name()}, {start_of_week.strftime('%Y-%m-%d')}, {name} worked more than {weekly_overtime} hours.")

                        # Set the flag for this week to True
                        printed_week[start_of_week] = True

                    elif total_hours < weekly_overtime:

                        # Group by date and sum the hours
                        hours = entries.groupby("Date")["Hours"].sum()

                        # Initialize a flag for each date
                        printed_day = {date: False for date in hours.index}

                        # Loop over the hours Series
                        for date, total_hours in hours.items():
                            # If the name is in the exceptions file, use 8 hours as the limit
                            if name == exceptions:
                                limit = 8
                            else:
                                limit = 10

                            # If the total hours are more than the limit and the statement has not been printed for this date
                            if total_hours > limit and not printed_day[date]:
                                # Print the name, total hours, and date without the time
                                print(f"{name} worked {total_hours} hours on {date.strftime('%Y-%m-%d')}, which is more than {limit} hours.")

                                # Set the flag for this date to True
                                printed_day[date] = True

# * this might be kinda a major issue we just deal with at another time
# ? what if no one works on monday?
# or the export doesnt start on a monday
else:
    print("The first day is not a Monday.")
    print("This may cause problems with the weekly overtime.")


