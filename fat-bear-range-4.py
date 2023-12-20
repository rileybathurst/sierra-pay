# create weeks


# this caluates if someone worked more than 40 hours in a week
import pandas as pd

sierra = pd.read_csv("Times_{date_str}.csv", )

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

    # Print the number of weeks
    print(f"There are {len(weeks)} weeks.")

    # Loop over each date in the sequence
    for start_of_week in weeks:
        # Generate a sequence of 7 days starting from the date
        week = pd.date_range(start=start_of_week, periods=7)

        # Initialize a flag for each week
        printed_week = {start_of_week: False for start_of_week in weeks}
        print(week)
        
    # Create a DataFrame from the weeks series
    weeks_df = pd.DataFrame(weeks, columns=["Week Start Date"])
    
    # Format the start and end dates as strings
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")
    
    # Write the DataFrame to a CSV file
    weeks_df.to_csv(f"exports/weeks_{start_date_str}_to_{end_date_str}.csv", index=False)


# * this might be kinda a major issue we just deal with at another time
# ? what if no one works on monday?
# or the export doesnt start on a monday
else:
    print("The first day is not a Monday.")
    print("This may cause problems with the weekly overtime.")


