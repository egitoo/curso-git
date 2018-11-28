import csv

f = open('teste.csv', 'r')

with f:

    reader = csv.reader(f)

    for row in reader:
        for e in row:
            print(e)