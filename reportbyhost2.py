import connectdb as con
from sys import exit 
from copy import deepcopy
from datetime import datetime
import optparse
import report2jira
from time import sleep

parser = optparse.OptionParser(version='0.1', usage="usage: %prog [options]")
parser.add_option("-j", "--jira", help="reg issue to jira") # -j 1
parser.add_option("-f", "--file", help="report filename .xls")

options,arguments=parser.parse_args()
jira=options.__dict__['jira']
input_files=options.__dict__['file'] ## maybe instead take the latest created xls file in the folder
# files = input_files.split(" ")

connect = con.nessus_db()

hosts = connect.query("Select DISTINCT host from scan ")

table_header="||Host||Port||CVE||Severity||Name||\n"
proj_name=""
table=""
host_strings=[]
for host in hosts:
	host_strings.append(host[0])
	res = connect.query("Select DISTINCT * from scan where host='"+str(host[0])+"' order by risk ASC")
	for line in res:
		if len(proj_name)<2:
			proj_name = line[14]
		if len(line[8])>2:
			prevrow = deepcopy(line)
			row="|"+line[5] + "|" + line[7]+"|"+line[2]+"&nbsp;|"+line[4]+"|"+line[8]+"|\n"
		else:
			row="|"+line[5] + "|" + line[7]+"|"+line[2]+"&nbsp;|"+line[4]+"|"+line[8]+"|\n"
		table+=row
		# print(proj_name)
	# exit()
cves = connect.query("Select DISTINCT CVE from scan")
cve_strings=[]
for cve in cves:
	cve_strings.append(cve[0])
print(table)
print(host_strings)
print(cve_strings)

tab = ""
if len(table) > 32767:
	tab = table[0:32767-len(table_header)]
else: 
	tab = table
# print(len(tab))
if jira:
	el = report2jira.Jira(proj_name+" security scan", table_header+tab, "\n".join(host_strings), input_files, "", "", proj_name.split("_")[0], "\n".join(cve_strings))
	#self, name, descr, hosts, files, md5, status, proj_name, cves
	issue = el.createIssue()
	el.makeItResolved(issue)
	print(issue)
	sleep(15)
connect.close_con()