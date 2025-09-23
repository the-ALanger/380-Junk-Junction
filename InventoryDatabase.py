import csv

with open('JJInventoryDatabase - Sheet1.csv', 'r') as file:
    reader = csv.reader(file)  # For comma-separated values
        # For tab-separated values, use: reader = csv.reader(file, delimiter='\t')
        
    for row in reader:
        print(row)