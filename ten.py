# add the hours together the test name worked on Nov 15

import csv

with open('.env', 'r') as f:
    for line in f:
        if 'test' in line:
            test = line.strip()

dates = []

with open('Timesheets Report.csv', newline='') as csvfile, open('exports/ten.csv', 'w', newline='') as output_file:
    reader = csv.reader(csvfile)
    writer = csv.writer(output_file)

    for row in reader:
      if len(row) > 2 and row[0] == test and row[1] == "Nov 15, 2023":
        writer.writerow(row)