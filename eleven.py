# add the hours together the tested name worked on a given date

import csv

with open('.env', 'r') as f:
    for line in f:
        if 'test' in line:
            test = line.strip()

dates = []

with open('Timesheets Report.csv', newline='') as csvfile, open('exports/eleven.csv', 'w', newline='') as output_file:
    reader = csv.reader(csvfile)
    writer = csv.writer(output_file)

    for row in reader:
      if len(row) > 2 and row[0] == test and row[1] not in dates:
        
        # creates the dates the test name worked
        writer.writerow([row[1]])
        dates.append(row[1])

        # adds the hours together
        total = 0
        csvfile.seek(0)
        for row in reader:
          if len(row) > 2 and row[0] == test and row[1] == dates[-1]:
            total += float(row[4])
        writer.writerow([total])
    writer.writerow([])