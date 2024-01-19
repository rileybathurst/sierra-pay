# https://www.dir.ca.gov/dlse/faq_overtime.htm
# shall not be employed more than eight hours in any workday or more than 40 hours in any workweek
# TODO: or more than six days in any workweek

# this isnt finished yet, need to figure out which is bigger of daily or weekly and if anyone exceeds 6 days

import pandas as pd
import datetime
import weeks

date_created = datetime.datetime.now()  # Get the current date and time
date_str = date_created.strftime("%Y-%m-%d")  # Format the date as a string

# print(f'Times_{date_str}.csv');  # Print the name of the file
sierra = pd.read_csv(f"Times_{date_str}.csv", )

# Convert the "Date" column to a datetime type
sierra["Date"] = pd.to_datetime(sierra["Date"])

# Get the earliest and latest dates
start_date = sierra["Date"].min()
end_date = sierra["Date"].max()

# Get the unique names
names = sierra["Name"].unique()

#seven_day_week per person
seven_day_weeks = {}

# Loop over each name
for name in names:
  
    seven_day_weeks[name] = []
  
    for i, week_start in enumerate(weeks.weeks, start=1):

      # Filter the entries for the current week and name
      week_entries = sierra[(sierra["Date"] >= week_start) & (sierra["Date"] < week_start + pd.DateOffset(days=7)) & (sierra["Name"] == name)]

      # Count the number of unique dates within the week
      num_days_with_entries = week_entries["Date"].dt.date.nunique()
      # print(f"Number of days with entries for {name} in week {i}: {num_days_with_entries}")
      
      if num_days_with_entries > 6:
        # Get the last day's work hours
        
        # add the entries into the dictionary
        # seven_day_weeks[name].append(week_start.date())
        
        # what is the last day of the week
        # print(week_start + pd.DateOffset(days=6))
        last_day_of_this_week = week_start + pd.DateOffset(days=6)
        
        # ! this is wrong end date needs to be of that week
        last_day_entries = sierra[(sierra["Date"] == last_day_of_this_week) & (sierra["Name"] == name)]
        # print(last_day_entries)
        
        seven_day_weeks[name].append("week starting " + str(week_start.date()) + " has a seventh day with " + str(last_day_entries.Hours.sum()) + " hours")
        
        
        # total_hours_last_day = last_day_entries["Hours"].sum()
        
        # print(f"{name} worked 7 days in week starting {week_start.date()}. Hours worked on the last day: {total_hours_last_day}")


# print(seven_day_weeks)

# Loop over each name and their corresponding seven-day weeks
for name, weeks in seven_day_weeks.items():
  # Check if there are any entries for this name
  if weeks:
    # Print the entries
    for entry in weeks:
      print(name, entry)
