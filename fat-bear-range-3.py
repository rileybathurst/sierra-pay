# create weeks


# this caluates if someone worked more than 40 hours in a week
import pandas as pd

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

    print(weeks)
    
else:
    print("The first day is not a Monday.")
    print("This may cause problems with the weekly overtime.")


