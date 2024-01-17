import pandas as pd
import datetime

# ! needs to be in .env file
exceptions = "Michelle Nino De Guzman"
test = "Adam Paul"

date_created = datetime.datetime.now()  # Get the current date and time
date_str = date_created.strftime("%Y-%m-%d")  # Format the date as a string

print(f'Times_{date_str}.csv');  # Print the name of the file

sierra = pd.read_csv(f"Times_{date_str}.csv", )

# sierra.head()

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

# Initialize a dictionary to store the total overtime hours for each name
total_overtime_hours = {}

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

      # If the total hours are more than 40
      if total_hours > 40:
        # Print the name, total hours, and week start date without the time
        print(f"{name} worked {total_hours} hours in the week starting {date.strftime('%Y-%m-%d')} ({date.day_name()}), which is more than 40 hours.")

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
      over = round(total_hours - limit, 4)

      # Print the date and how much over they were
      print(f"On {date.date()}, {name} worked {over} hours over {limit} hours.")
      
      # Add the overtime hours to the total overtime hours for the name
      if name in total_overtime_hours:
        total_overtime_hours[name] += over
      else:
        total_overtime_hours[name] = over

# Print the total overtime hours for each name
for name, overtime_hours in total_overtime_hours.items():
  print(f"{name} worked a total of {round(overtime_hours, 2)} overtime hours.")
