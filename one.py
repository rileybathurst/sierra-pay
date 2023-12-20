# basic start read something in a csv file and write it out to another csv file
import csv

with open('.env', 'r') as f:
    for line in f:
        if 'test' in line:
            test = line.strip()

print("TOP LEVEL IN ONE.PY")

with open('Timesheets Report.csv', 'r') as file, open('output.csv', 'w', newline='') as output_file:
    
    reader = csv.reader(file)
    writer = csv.writer(output_file)

    for row in reader:
        for cell in row:
            if test in cell:
                print(row)
                writer.writerow(row)