import csv

names = []
overtime = 10
dates = []
exceptions = "Michelle Nino De Guzman"
overtime_8 = 8

with open('Timesheets Report.csv', newline='') as csvfile, open('exports/overtime.csv', 'w', newline='') as output_file:
  reader = csv.reader(csvfile)
  writer = csv.writer(output_file)
  
  writer.writerow(['Name','Date','Overtime'])
  writer.writerow(["Overtime", overtime , "hours per day"])
  writer.writerow(["Except ", exceptions , overtime_8,  "hours per day"])
  
  # names
  for row in reader:
    if len(row) == 2 and 'Total Hours' not in row[0]: # this is how we know its a name and a number
      number = float(row[1])
      if number > 0:
        names.append(row[0])
  csvfile.seek(0)
  
  for name in names:
    overtime_dict = {name + '_overtime': False for name in names}
    # row_dict = {name + '_row': False for name in names}

  # Dates
  for row in reader:
    if len(row) > 2 and row[1] not in dates and row[1] != 'Date' and row[0] != 'Report totals:':
      dates.append(row[1])
      # print(row[1])
  csvfile.seek(0)

  writer.writerow(['Start date', dates[0]]);
  writer.writerow(['End date', dates[-1]]);
  writer.writerow([]);
  
  for name in names:
      if name == exceptions:
          overtime = overtime_8

      for date in dates:
          total = 0

          for row in reader:
              if date in row and name in row and len(row) > 3:
                  total += float(row[4])

          if total > overtime:
              writer.writerow([name, date, round(total-overtime, 3)])
              
              overtime_dict[name] = True

          csvfile.seek(0)

      # for name, has_overtime in overtime_dict.items():
        # if has_overtime:
          # print(name)
          # row_dict[name] = True # TODO: I couldnt get this to add blank lines

      csvfile.seek(0)
