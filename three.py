# do something with a file thats been created
import csv

print("TOP LEVEL IN ONE.PY")

with open('Timesheets Report.csv', 'r') as file, open('adam.csv', 'w', newline='') as output_file, open('riley.csv', 'w', newline='') as output_file2:
    reader = csv.reader(file)

    for row in reader:
        for cell in row:
            if 'Adam Paul' in cell:
                # print(row)
                csv.writer(output_file).writerow(row)

            if 'Riley Bathurst' in cell:
                # print(row)
                csv.writer(output_file2).writerow(row)

with open('riley.csv', 'r') as file:
    reader = csv.reader(file)
    riley_file = list(reader)

    for row in riley_file:
        print(row)