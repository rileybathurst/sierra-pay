# do five.py but use an array of names to search for

import csv

names = ['Adam Paul', 'Riley Bathurst']

with open('Timesheets Report.csv', 'r') as input_file, open('exports/six.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    for name in names:
      for row in reader:
        if name in row:
          writer.writerow(row)

      writer.writerow([])
      input_file.seek(0)  # Reset the file pointer to the beginning