# if theres a number in column B, print the name in column A
# slowly working towrds grab all the nameds for me
# then check if they worked any hours

import csv

with open('.env', 'r') as f:
    for line in f:
        if 'test' in line:
            test = line.strip()

with open('Timesheets Report.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        if row != '':
          for cell in row:
            if test in cell:
              # print(row.index(cell)) # this says the test name is in column 0
              # print(row[0])
              # print(row[1])
              if(row[1] == "17.5"): # means these are strings
                print(row[0])