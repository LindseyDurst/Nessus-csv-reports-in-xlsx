# Nessus-csv-reports-in-xlsx

################################<br/>
DO<br/>
python3 movecsv2db.py -f file.csv<br/>
python3 formexcel.py <br/>
python3 paint.py -f file.xls<br/>
################################<br/>
REPORT TO JIRA<br/>
*change creds in files*<br/>
*first need to get scan info into the database*<br/><br/>
python3 movecsv2db.py -f file.csv<br/>
python3 reportbyhost2.py -j file.xls -j 1<br/>

