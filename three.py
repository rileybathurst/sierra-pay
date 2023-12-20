# do something with a file thats been created
import csv

with open('.env', 'r') as f:
    for line in f:
        if 'test' in line:
            test = line.strip()

with open('Timesheets Report.csv', 'r') as file, open('hours-3.csv', 'w', newline='') as output_file, open('test-3.csv', 'w', newline='') as output_file2:
    reader = csv.reader(file)

    for row in reader:
        for cell in row:
            if '206.65' in cell:
                # print(row)
                csv.writer(output_file).writerow(row)

            if test in cell:
                # print(row)
                csv.writer(output_file2).writerow(row)

with open('test-3.csv', 'r') as file, open('test-jobs.csv', 'w', newline='') as output_file3:
    reader = csv.reader(file)
    test_file = list(reader)

    for row in test_file:
        for cell in row:
            if 'Job #' in cell:
                # print(row)
                csv.writer(output_file3).writerow(row)