# hard coded to adam how many hours per day

import csv

names = []
overtime = 10 # so I can test it
dates = []

with open('Timesheets Report.csv', newline='') as csvfile, open('exports/twelve.csv', 'w', newline='') as output_file:
  reader = csv.reader(csvfile)
  writer = csv.writer(output_file)
  
  for row in reader:
    if len(row) == 2 and 'Total Hours' not in row[0]: # this is how we know its a name and a number
      # print(row[0]) # print the name

      number = float(row[1])
      if number > 0:
        names.append(row[0])
  csvfile.seek(0)

  for row in reader:
    if len(row) > 2 and row[0] == 'Adam Paul' and row[1] not in dates:
      
      # creates the dates adam worked
      # writer.writerow([row[1]])
      # writer.writerow([])
      dates.append(row[1])
  csvfile.seek(0)
  
  # print(dates);
  # print(dates[0]);
  # print(dates[-1]);
  writer.writerow(['Start date ', dates[0]]);
  writer.writerow([dates[-1]]);
  
  for name in names:
    # writer.writerow([name])
    for date in dates:
      # print(date)
      # writer.writerow([date])
      total = 0

      for row in reader:
        
        if date in row and name in row:
          # writer.writerow(row)
          total += float(row[4])
        
      if total > overtime:
        # writer.writerow(["Daily Hours",total])
        writer.writerow([name,date,round(total-overtime, 2)])# this does a weird remainder
      # else:
        # writer.writerow(["Daily Hours",total])
      
      # writer.writerow([])

      csvfile.seek(0)
    csvfile.seek(0)

