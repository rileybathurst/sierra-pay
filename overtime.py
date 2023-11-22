import csv
import datetime
# from dotenv import load_dotenv

# load_dotenv()  # Load the .env file

# Get the string from the environment variable
# my_string = os.getenv('MY_STRING')

names = []
overtime = 10
dates = []
exceptions = "Michelle Nino De Guzman" # ! this needs to be in a hidden file

overtime_8 = 8
date_created = datetime.datetime.now()  # Get the current date and time
date_str = date_created.strftime("%Y-%m-%d")  # Format the date as a string

with open('Timesheets Report.csv', newline='') as csvfile, open(f'exports/overtime_{date_str}.csv', 'w', newline='') as output_file:
  reader = csv.reader(csvfile)
  writer = csv.writer(output_file)
  
  writer.writerow(["Overtime Calculator"])
  
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
  
  sorted_dates = sorted([datetime.datetime.strptime(date, "%b %d, %Y") for date in dates])
  dates = [date.strftime("%b %d, %Y") for date in sorted_dates]
  
  
  writer.writerow(['Date Range', dates[0], dates[-1]]);
  writer.writerow([]);
  
  writer.writerow(["Overtime", overtime , "hours per day"])
  writer.writerow([exceptions , overtime_8,  "hours per day"])
  writer.writerow([]);
  
  writer.writerow(['Name','Date','Overtime'])
  
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
