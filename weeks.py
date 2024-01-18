# I need to organize this by weeks starting on Monday

import pandas as pd
import datetime

date_created = datetime.datetime.now()  # Get the current date and time
date_str = date_created.strftime("%Y-%m-%d")  # Format the date as a string

print(f'Times_{date_str}.csv');  # Print the name of the file

try:
  sierra = pd.read_csv(f"Times_{date_str}.csv", )

except FileNotFoundError:
  print("File not found. You may need to run the first file.")

# Convert the "Date" column to a datetime type
sierra["Date"] = pd.to_datetime(sierra["Date"])

# Get the earliest and latest dates
sheet_start_date = sierra["Date"].min()
sheet_end_date = sierra["Date"].max()

print(f"The earliest date is {sheet_start_date.date()}.")
print(f"The latest date is {sheet_end_date.date()}.")

# Get the day of the week for the start date
sheet_start_day = sheet_start_date.day_name()

if sheet_start_day == "Monday":
  print("The start date is a Monday.")
  
  first_monday = sheet_start_date
    
else:
  print("The start date is not a Monday.")

  # Find the first Monday
  first_monday = sheet_start_date + pd.DateOffset(days=(6 - sheet_start_date.weekday() + 1) % 7)
  print(f"The first Monday is {first_monday.date()}.")

# Generate a sequence of weeks with 7 days in each
weeks = pd.date_range(start=first_monday, end=sheet_end_date, freq='7D')
# print(weeks)

# Check if sheet_end_date is 6 days more than the start of the last week
last_week_start = weeks[-1]  # Get the start date of the last week

# Calculate the number of days between last_week_start and sheet_end_date
days_between = (sheet_end_date.date() - last_week_start.date()).days
# print(f"The number of days between the last week that starts on {last_week_start.strftime('%Y-%m-%d')} and last day on the sheet {sheet_end_date.strftime('%Y-%m-%d')} is {days_between}.")

# If the number of days is 7, then the last week is complete
if days_between == 7:
  print("The last week is complete.")
  
else:
  print("The last week is not complete. Removing it from the set of weeks.")
  weeks = weeks[:-1]  # Remove the last week
  
if len(weeks) == 0:
  print("There are no full weeks.")
elif len(weeks) == 1:
  print("There is 1 full week.")
else:
  print(f"There are {len(weeks)} full weeks.")
  
for i, week_start in enumerate(weeks, start=1):
    print(f"Week {i} starts on {week_start.date()}")
