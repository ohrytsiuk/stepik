import csv
import collections
import time

date = []

with open('Crimes.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        crime = time.strftime(row.get('Date'))
        if '2015' in crime:
            date.append(row.get('Primary Type'))
    n = collections.Counter(date).most_common()
    print(n[0])
