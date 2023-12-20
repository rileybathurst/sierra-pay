import csv
import datetime

date_created = datetime.datetime.now()  # Get the current date and time
date_str = date_created.strftime("%Y-%m-%d")  # Format the date as a string

header = "Name"

with open('Timesheets Report.csv', newline='') as csvfile, open(f'exports/Times_{date_str}.csv', 'w', newline='') as output_file:
    reader = csv.reader(csvfile)
    writer = csv.writer(output_file)

    # Skip rows until the header row is found
    for row in reader:
        if header in row:
            break

    # Write the header row to the output file
    writer.writerow(row)

    # Write the remaining rows to the output file
    for row in reader:
        writer.writerow(row)