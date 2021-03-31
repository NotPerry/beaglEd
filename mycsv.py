import csv

with open('THEcsv.csv', 'w') as f:
    fieldname = ['path', 'hash']
    writer = csv.DictWriter(f, fieldnames=fieldname)

    writer.writeheader()
    writer.writerow({'path':'1234', 'hash':'78910'})
