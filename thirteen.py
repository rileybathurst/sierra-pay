import csv
import datetime

names = []
overtime = 40
dates = []
date_created = datetime.datetime.now()  # Get the current date and time
date_str = date_created.strftime("%Y-%m-%d")  # Format the date as a string

with open('Timesheets Report.csv', newline='') as csvfile, open(f'exports/thirteen_{date_str}.csv', 'w', newline='') as output_file:
  reader = csv.reader(csvfile)
  writer = csv.writer(output_file)

  # Dates
  for row in reader:
    if len(row) > 2 and row[1] not in dates and row[1] != 'Date' and row[0] != 'Report totals:':
      dates.append(row[1])
      # print(row[1])
  csvfile.seek(0)
  
  sorted_dates = sorted([datetime.datetime.strptime(date, "%b %d, %Y") for date in dates])
  dates = [date.strftime("%b %d, %Y, %A") for date in sorted_dates]
  
  # names
  for row in reader:
    if len(row) == 2 and 'Total Hours' not in row[0]:
      number = float(row[1])
      if number > 0:
        names.append(row[0].lower())
  csvfile.seek(0)
  
  for name in names:
    weekly_time = {name + '_weekly': 0 for name in names}
  csvfile.seek(0)
  
  for name in names:
    # print(name)
    for row in reader:
            
        if name.lower() in (item.lower() for item in row) and len(row) > 3:
          # print(name, row)
            weekly_time[f'{name}_weekly'] += float(row[4])
    csvfile.seek(0)

  for name, time in weekly_time.items():
    # print(f"{name}: {time}")
    writer.writerow([name, round(time, 3)])