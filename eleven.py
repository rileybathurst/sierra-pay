# add the hours together adam worked on a given date

import csv

dates = []

with open('Timesheets Report.csv', newline='') as csvfile, open('exports/eleven.csv', 'w', newline='') as output_file:
    reader = csv.reader(csvfile)
    writer = csv.writer(output_file)

    for row in reader:
      if len(row) > 2 and row[0] == 'Adam Paul' and row[1] not in dates:
        
        # creates the dates adam worked
        writer.writerow([row[1]])
        dates.append(row[1])

        # adds the hours together
        total = 0
        csvfile.seek(0)
        for row in reader:
          if len(row) > 2 and row[0] == 'Adam Paul' and row[1] == dates[-1]:
            total += float(row[4])
        writer.writerow([total])
    writer.writerow([])