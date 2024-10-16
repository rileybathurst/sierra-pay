# %%
import os

input_file = "/Users/rileybathurst/Developer/sierra-pay/Timesheets Report.csv"
output_file = "/Users/rileybathurst/Developer/sierra-pay/Timesheets Report Cleaned.csv"

with open(input_file, 'r') as file:
  lines = file.readlines()

# Find the line starting with "Name"
start_index = next(i for i, line in enumerate(lines) if line.startswith("Name"))

# Write the lines from the "Name" line onwards to the new file
with open(output_file, 'w') as file:
  file.writelines(lines[start_index:])

# %%
