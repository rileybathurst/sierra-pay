# I need to organize this by weeks starting on Monday

import pandas as pd
import datetime

date_created = datetime.datetime.now()  # Get the current date and time
date_str = date_created.strftime("%Y-%m-%d")  # Format the date as a string

print(f'Times_{date_str}.csv');  # Print the name of the file

sierra = pd.read_csv(f"Times_{date_str}.csv", )

# Convert the "Date" column to a datetime type
sierra["Date"] = pd.to_datetime(sierra["Date"])

# Get the earliest and latest dates
sheet_start_date = sierra["Date"].min()
sheet_end_date = sierra["Date"].max()

# print(f"The earliest date is {sheet_start_date.date()}.")
print(f"The latest date is {sheet_end_date.date()}.")

# Get the day of the week for the start date
sheet_start_day = sheet_start_date.day_name()

if sheet_start_day == "Monday":
  print("The start date is a Monday.")

  # Generate a sequence of weeks with 7 days in each
  weeks = pd.date_range(start=sheet_start_date, end=sheet_end_date, freq='7D')
  print(weeks)

  # Check if sheet_end_date is 6 days more than the start of the last week
  last_week_start = weeks[-1]  # Get the start date of the last week

  # Calculate the number of days between last_week_start and sheet_end_date
  days_between = (sheet_end_date.date() - last_week_start.date()).days
  print(f"The number of days between the last week that starts on {last_week_start.strftime('%Y-%m-%d')} and last day on the sheet {sheet_end_date.strftime('%Y-%m-%d')} is {days_between}.")

  # If the number of days is 7, then the last week is complete
  if days_between == 7:
    print("The last week is complete.")
    
  else:
    print("The last week is not complete. Removing it from the set of weeks.")
    weeks = weeks[:-1]  # Remove the last week
    
else:
  print("The start date is not a Monday.")
  
  # TODO: Add code to handle this case