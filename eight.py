# if theres a number in column B, print the name in column A
# slowly working towrds grab all the nameds for me
# then check if they worked any hours

import csv

names = []

with open('Timesheets Report.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
      if len(row) == 2 and 'Total Hours' not in row[0]: # this is how we know its a name and a number
        # print(row[0]) # print the name
        names.append(row[0])

print(names)