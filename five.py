import csv

with open('Timesheets Report.csv', 'r') as input_file, open('exports/five.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    for row in reader:
        if 'Adam Paul' in row:
            writer.writerow(row)

    writer.writerow([])

    input_file.seek(0)  # Reset the file pointer to the beginning
    for row in reader:
        if 'Riley Bathurst' in row:
            writer.writerow(row)
