# create a file of who worked hours this period

import csv

names = []

with open('Timesheets Report.csv', newline='') as csvfile, open('exports/nine.csv', 'w', newline='') as output_file:
    reader = csv.reader(csvfile)
    writer = csv.writer(output_file)
    
    for row in reader:
      if len(row) == 2 and 'Total Hours' not in row[0]: # this is how we know its a name and a number
        # print(row[0]) # print the name

        number = float(row[1])
        if number > 0:
          names.append(row[0])
          writer.writerow([row[0]])
          writer.writerow([])

# print(names)
# writer.writerow(row)