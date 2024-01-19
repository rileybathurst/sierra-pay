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

non_week_dates = []

week_numbers = {}

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
dates_between = pd.date_range(start=last_week_start.date(), end=sheet_end_date.date())

print(f"The number of days between the last week that starts on {last_week_start.strftime('%Y-%m-%d')} and last day on the sheet {sheet_end_date.strftime('%Y-%m-%d')} is {len(dates_between)}.")

# If the number of days is 7, then the last week is complete
if len(dates_between) == 7:
  print("The last week is complete.")
  
else:
  # add all dates in dates_between to non_week_dates
  for date in dates_between:
    non_week_dates.append(date)
  
  print("The last week is not complete. Removing it from the set of weeks.")
  weeks = weeks[:-1]  # Remove the last week
  
if len(weeks) == 0:
  print("There are no full weeks.")
elif len(weeks) == 1:
  print("There is 1 full week.")
else:
  print(f"There are {len(weeks)} full weeks.")
  
for i, week_start in enumerate(weeks, start=1):
    print(f"Week {i} starts on {week_start.day_name()}, {week_start.date()}")
    
    week_numbers["week_" + str(i)] = []
    week_numbers["week_" + str(i)].append(week_start.date())
    
    for days in range(1, 7):
      # print(week_start + pd.DateOffset(days=days))
      additional_date = week_start + pd.DateOffset(days=days)
      week_numbers["week_" + str(i)].append(additional_date.date())
      
# print(week_numbers) # this is a dictionary
# print(week_numbers['week_2']) # this is an array of dates

# create a dictionary to hold the varibles
week_daily_overtime = {}

#TODO: this is going to need names invloved
for week in week_numbers:
    # create a variable for each week with the name of the week and _daily_overtime
  week_daily_overtime[str(week) + '_daily_overtime'] = 0

print(week_daily_overtime)

# Generate a sequence of all dates from the start date to the end date
all_dates = pd.date_range(start=sheet_start_date, end=sheet_end_date)

for date in all_dates:
    # Check if the date is before the first Monday
    if date < first_monday:
        non_week_dates.append(date)
        
if len(non_week_dates) > 0:
    print("Dates outside the weeks specified:")
    for date in non_week_dates:
        print(date.date())
else:
    print("There are no dates outside the weeks specified.")
