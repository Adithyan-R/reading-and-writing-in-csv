# writing to CSV
import csv
'''

	
# field names
fields = ['Name', 'Experience']
	
# data rows of csv file
rows = [ ['Nikhil',  '2'],
		['Sanchit', '2'],
		['Aditya', '2'],
		['Sagar',  '1' ],
		['Prateek',  '3' ],
		['Sahil',  '2']]
	
# name of csv file
filename = "records.csv"
	
# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
		
	# writing the fields
	csvwriter.writerow(fields)
		
	# writing the data rows
	csvwriter.writerows(rows)
'''

#Writing a dictionary to a CSV file

# data rows as dictionary objects
mydict =[{ 'Name': 'John', 'Experience': '3'},
		{ 'Name': 'Paul', 'Experience': '2'},
        { 'Name': 'Victor', 'Experience': '4'},]
	
# field names
fields = ['Name','Experience']
	
# name of csv file
filename = "records1.csv"
	
# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv dict writer object
	writer = csv.DictWriter(csvfile, fieldnames = fields)
		
	# writing headers (field names)
	writer.writeheader()
		
	# writing data rows
	writer.writerows(mydict)

csvfile.close()

# opening the CSV file
with open('records.csv', mode ='r')as file:
    # reading the CSV file
    csvfile= csv.reader(file)
'''
# displaying the contents of the CSV file
for lines in csvfile:
    print(lines)
'''


