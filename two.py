# read in a csv file and write it out to two seperate csv files with pattern matching
import csv

with open('.env', 'r') as f:
    for line in f:
        if 'test' in line:
            test = line.strip()

print("TOP LEVEL IN ONE.PY")

with open('Timesheets Report.csv', 'r') as file, open('test.csv', 'w', newline='') as output_file, open('test2.csv', 'w', newline='') as output_file2:
    reader = csv.reader(file)

    for row in reader:
        for cell in row:
            if test in cell:
                # print(row)
                csv.writer(output_file).writerow(row)

            if test2 in cell:
                # print(row)
                csv.writer(output_file2).writerow(row)

with open('test2.csv', 'r') as file:
    reader = csv.reader(file)
    test2_file = list(reader)

    for row in test2_file:
        print(row)