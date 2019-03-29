import connectdb as con
import sys
import csv
import glob
import xlwt


connect = con.nessus_db()


res = connect.query("Select * from scan order by plugin_id, risk DESC")

book = xlwt.Workbook()
sh = book.add_sheet('Vulnerability scan',cell_overwrite_ok=True)

sh.row(0).write(0, 'Plugin ID')
sh.row(0).write(1, 'CVE')
sh.row(0).write(2, 'CVSS')
sh.row(0).write(3, 'Risk')
sh.row(0).write(4, 'Host')
sh.row(0).write(5, 'Protocol')
sh.row(0).write(6, 'Port')
sh.row(0).write(7, 'Name')
sh.row(0).write(8, 'Synopsis')
sh.row(0).write(9, 'Description')
sh.row(0).write(10, 'Solution')
sh.row(0).write(11, 'See Also')
sh.row(0).write(12, 'Plugin Output')

output_name=res[0][14]+"-unmerged.xls"
print(output_name)
i=1
for row in res:
	sh.row(i).write(0, row[1])
	sh.row(i).write(1, row[2])
	sh.row(i).write(2, row[3])
	sh.row(i).write(3, row[4])
	sh.row(i).write(4, row[5])
	sh.row(i).write(5, row[6])
	sh.row(i).write(6, row[7])
	sh.row(i).write(7, row[8])
	sh.row(i).write(8, row[9])
	sh.row(i).write(9, row[10])
	sh.row(i).write(10, row[11])
	sh.row(i).write(11, row[12])
	sh.row(i).write(12, row[13])
	i+=1

book.save(output_name)

print(output_name)