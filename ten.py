# add the hours together adam worked on Nov 15

import csv

dates = []

with open('Timesheets Report.csv', newline='') as csvfile, open('exports/ten.csv', 'w', newline='') as output_file:
    reader = csv.reader(csvfile)
    writer = csv.writer(output_file)

    for row in reader:
      if len(row) > 2 and row[0] == 'Adam Paul' and row[1] == "Nov 15, 2023":
        writer.writerow(row)