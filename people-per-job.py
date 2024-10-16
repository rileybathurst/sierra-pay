# first try just divide by number of people
# this involves adding new columns

#%%

import os
import pandas as pd
import datetime

folder = "/Users/rileybathurst/Developer/sierra-pay"

date_created = datetime.datetime.now()  # Get the current date and time
date_str = date_created.strftime("%Y-%m-%d")  # Format the date as a string

os.makedirs(date_str, exist_ok=True)

input_file = f"{folder}/Timesheets Report.csv"
output_file = f"{folder}/{date_str}/Timesheets Report Cleaned.csv"

with open(input_file, 'r') as file:
  lines = file.readlines()

# Find the line starting with "Name"
start_index = next(i for i, line in enumerate(lines) if line.startswith("Name"))

# Write the lines from the "Name" line onwards to the new file
with open(output_file, 'w') as file:
  file.writelines(lines[start_index:])

sierra = pd.read_csv(f"{folder}/{date_str}/Timesheets Report Cleaned.csv", )

# print(sierra.head())

filtered_sierra = sierra[sierra["Working on"] != "General"]

lei = filtered_sierra[sierra['Working on'] == 'Job #982 - Leimomi  Lammerding']
print(lei.head())

unique_jobs = filtered_sierra['Working on'].unique()

for job in unique_jobs:
  job_data = filtered_sierra[filtered_sierra['Working on'] == job]
  # job_name = job.replace(" ", "_")
  
  # Lei is interesting as 4 jobs but only 3 people
  num_people = job_data['Name'].nunique()
  print(f"Job: {job}, Number of unique people: {num_people}")
  
  # Add a new row with the number of unique people
  installer_row = [None] * len(job_data.columns)
  installer_row[:2] = ['Number of installers', num_people]  # Assuming column 1 is the first column (index 0) and column 2 is the second column (index 1)
  job_data.loc[len(job_data)] = installer_row
  
  total_hours = job_data['Hours'].sum()
  total_hours_row = [None] * len(job_data.columns)
  total_hours_row[:2] = ['Total Hours', total_hours]
  job_data.loc[len(job_data)] = total_hours_row
  
  # Calculate the percent of install time for each row
  job_data['Percent of Install Time'] = (job_data['Hours'] / total_hours) * 100
  
  # Add a blank column at the end
  job_data['Total Percent of Install Time'] = None
  
  # Group by 'Name' and sum the 'Percent of Install Time'
  percent_install_time_sum = job_data.groupby('Name')['Percent of Install Time'].sum().reset_index()

  # Merge the summed percent install time back into the original dataframe
  job_data = job_data.merge(percent_install_time_sum, on='Name', suffixes=('', '_Total'))

  # Update the 'Total Percent of Install Time' column with the summed values
  job_data['Total Percent of Install Time'] = job_data['Percent of Install Time_Total']

  # Drop the temporary 'Percent of Install Time_Total' column
  job_data.drop(columns=['Percent of Install Time_Total'], inplace=True)
  
  job_data.to_csv(f"{folder}/{date_str}/{job}.csv", index=False)


# %%
