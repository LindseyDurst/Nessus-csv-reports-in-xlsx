import connectdb as con
import sys
import optparse
import csv

## Setting parameters ##
parser = optparse.OptionParser(version='0.1', usage="usage: %prog [options] file")
parser.add_option("-f", "--file", help="input file name .csv")

options,arguments=parser.parse_args()
input_file=options.__dict__['file']

proj=input_file[0:len(input_file)-4]

connect = con.nessus_db()
connect.create_table() # if you need to reset your database
rowlist=[]
with open(input_file) as report:
	csvfile = csv.DictReader(report)
	for row in csvfile:
		temprow=[int(row['Plugin ID']),row['CVE'],row['CVSS'],row['Risk'],row['Host'], row['Protocol'],row['Port'],row['Name'],row['Synopsis'],row['Description'],row['Solution'],row['See Also'],row['Plugin Output'],proj]
		rowlist.append(temprow)


for insertlist in rowlist:
	connect.insert(insertlist)
connect.close_con()
print("Data inserted into db")
