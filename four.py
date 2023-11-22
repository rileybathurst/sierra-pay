# do something with variables
import csv

myint = 7
print(myint)

# loops
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

with open('Timesheets Report.csv', 'r') as file, open('hours-3.csv', 'w', newline='') as output_file, open('riley-3.csv', 'w', newline='') as output_file2:
    reader = csv.reader(file)

    for row in reader:
        for cell in row:
            if '206.65' in cell:
                # print(row)
                csv.writer(output_file).writerow(row)

            if 'Riley Bathurst' in cell:
                # print(row)
                csv.writer(output_file2).writerow(row)

with open('riley-3.csv', 'r') as file, open('riley-jobs.csv', 'w', newline='') as output_file3:
    reader = csv.reader(file)
    riley_file = list(reader)

    for row in riley_file:
        for cell in row:
            if 'Job #' in cell:
                # print(row)
                csv.writer(output_file3).writerow(row)