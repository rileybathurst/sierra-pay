# basic start read something in a csv file and write it out to another csv file
import csv

print("TOP LEVEL IN ONE.PY")

with open('Timesheets Report.csv', 'r') as file, open('output.csv', 'w', newline='') as output_file:
    
    reader = csv.reader(file)
    writer = csv.writer(output_file)

    for row in reader:
        for cell in row:
            if 'Adam Paul' in cell:
                print(row)
                writer.writerow(row)