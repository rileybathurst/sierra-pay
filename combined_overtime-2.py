# https://www.dir.ca.gov/dlse/faq_overtime.htm
# shall not be employed more than eight hours in any workday or more than 40 hours in any workweek
# or more than six days in any workweek

# this isnt finished yet, need to figure out which is bigger of daily or weekly and if anyone exceeds 6 days

import pandas as pd
import datetime
import weeks

# ! needs to be in .env file
exceptions = "Michelle Nino De Guzman"
test = "Adam Paul"

date_created = datetime.datetime.now()  # Get the current date and time
date_str = date_created.strftime("%Y-%m-%d")  # Format the date as a string

# print(f'Times_{date_str}.csv');  # Print the name of the file

sierra = pd.read_csv(f"Times_{date_str}.csv", )

# sierra.head()

# Convert the "Date" column to a datetime type
sierra["Date"] = pd.to_datetime(sierra["Date"])

# Get the earliest and latest dates
start_date = sierra["Date"].min()
end_date = sierra["Date"].max()

# Get the unique names
names = sierra["Name"].unique()

# Generate a sequence of all dates from the start date to the end date
all_dates = pd.date_range(start=start_date, end=end_date)

# Initialize a dictionary to store the total overtime hours for each name
total_overtime_hours = {}

# Initialize a list to store the names and weeks of people with overtime
overtime_details = []

# Loop over each name
for name in names:
  if name == "Bex Howard":
  
    for i, week_start in enumerate(weeks.weeks, start=1):

      # Filter the entries for the current week and name
      week_entries = sierra[(sierra["Date"] >= week_start) & (sierra["Date"] < week_start + pd.DateOffset(days=7)) & (sierra["Name"] == name)]
      
      # Sum the hours for the week
      total_weekly_hours = week_entries["Hours"].sum()

      # If the total hours are more than 40
      if total_weekly_hours > 40:
        # Print the name, total hours, and week start date without the time
        weekly_overtime_hours = total_weekly_hours - 40
        # print(f"{name} worked {total_weekly_hours} hours in the week starting {date.strftime('%Y-%m-%d')} ({date.day_name()}), which is {round(weekly_overtime_hours, 2)} hours of overtime.")
        print(f"{name} worked {total_weekly_hours} hours in the week starting {week_start.date()} ({week_start.day_name()}), which is {round(weekly_overtime_hours, 2)} hours of overtime.")