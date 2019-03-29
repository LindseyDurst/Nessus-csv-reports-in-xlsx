import sqlite3

class nessus_db:
	def __init__(self):
		self.conn = sqlite3.connect('nessus1.db')
		self.c = self.conn.cursor()
		self.table_name="scan"

	def create_table(self):
		# self.table_name=proj
		self.c.execute("Drop table if exists %s" % self.table_name)
		self.c.execute("CREATE TABLE %s (id INTEGER PRIMARY KEY AUTOINCREMENT, plugin_id INTEGER, cve text, cvss text, risk text, host text, protocol text, port text, name text, synopsis text, description text, solution text, also text, plug_output text,project_name text)"% self.table_name)
	def insert(self, data_row):
		self.c.execute("INSERT INTO %s VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"%self.table_name, data_row)
		self.conn.commit()
	def get1res(self, id):
		t = str(id)
		self.c.execute('SELECT * FROM %s WHERE id=?'%self.table_name, t)
		return self.c.fetchone()
	def query(self,query):
		# print(query)
		self.c.execute(query)
		return self.c.fetchall()
	def create_new_table(self, name):
		self.c.execute("Drop table if exists %s" % name)
		self.c.execute("CREATE TABLE %s (id INTEGER PRIMARY KEY AUTOINCREMENT, plugin_id INTEGER, cve text, cvss text, risk text, host text, protocol text, port text, name text, synopsis text, description text, solution text, also text, plug_output text,project_name text)"% name)
	def close_con(self):
		self.conn.close()

# test = nessus_db()
# test.create_table_d()
# insertlist=['000000', '10.0', 'Critical', 'virexch0', 'tcp', '0', 'Active Outbound Connection to Host Listed in Known Bot Database', 'The remote host is making an outbound connection to a host that is listed as part of a botnet, according to a third-party public database.', 'Nessus has determined via netstat, that the remote host has an outbound connection to one or more hosts that are listed in a public database as part of a botnet. This suggests the host may have been\ncompromised.', 'Investigate the connection(s) and reinstall the remote system from\nscratch if appropriate.', '', 'The host has outbound connections to the following IP addresses that are flagged as part of a botnet :\nIP address   : 94.102.50.42\nDate flagged : 28/Sep/2017\n\nIP address   : 80.82.67.186\nDate flagged : 28/Sep/2017','']
# test.insert_d(insertlist)