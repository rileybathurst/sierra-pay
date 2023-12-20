# This script will take a csv file and return the date range of the file.

import csv
import datetime

dates = []

with open('Timesheets Report.csv', newline='') as csvfile:
  reader = csv.reader(csvfile)

  # Dates
  for row in reader:
    if len(row) > 2 and row[1] not in dates and row[1] != 'Date' and row[0] != 'Report totals:':
      dates.append(row[1])
  csvfile.seek(0)
  
  sorted_dates = sorted([datetime.datetime.strptime(date, "%b %d, %Y") for date in dates])
  dates = [date.strftime("%m_%d_%Y") for date in sorted_dates]

  print('Timesheets Report ' + dates[0] + '-' + dates[-1] + '.csv')
