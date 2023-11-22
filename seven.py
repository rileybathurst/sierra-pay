# if theres a number in column B, print the name in column A
# slowly working towrds grab all the nameds for me
# then check if they worked any hours

import csv

with open('Timesheets Report.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        if row != '':
          for cell in row:
            if 'Adam Paul' in cell:
              # print(row.index(cell)) # this says adam paul is in column 0
              # print(row[0])
              # print(row[1])
              if(row[1] == "17.5"): # means these are strings
                print(row[0])