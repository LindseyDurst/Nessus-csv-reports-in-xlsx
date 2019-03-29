# Nessus-csv-reports-in-xlsx

################################
DO
python3 movecsv2db.py -f file.csv
python3 formexcel.py 
python3 paint.py -f file.xls
################################
REPORT TO JIRA
*change creds in files*
*first need to get scan info into the database*

python3 movecsv2db.py -f file.csv
python3 reportbyhost2.py -j file.xls -j 1

