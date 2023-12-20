import csv

with open('.env', 'r') as f:
    for line in f:
        if 'test' in line:
            test = line.strip()

with open('.env', 'r') as f:
    for line in f:
        if 'test' in line:
            test = line.strip()

with open('Timesheets Report.csv', 'r') as input_file, open('exports/five.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    for row in reader:
        if test in row:
            writer.writerow(row)

    writer.writerow([])

    input_file.seek(0)  # Reset the file pointer to the beginning
    for row in reader:
        if test in row:
            writer.writerow(row)
