import csv

# opening the CSV file
with open('records.csv', mode ='r')as file:
    # reading the CSV file
    csvfile= csv.reader(file)
    for lines in csvfile:
        print(lines)
# displaying the contents of the CSV file



