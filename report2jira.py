import sys
from jira import JIRA
import os

class Jira:

	
	config={'username':'USER','password':'PASS'}
	
	def __init__(self, name, descr, hosts, files, md5, status, proj_name, cves):
		self.proxies = {
			'http': 'http://127.0.0.1:8080',
			'https': 'https://127.0.0.1:8080',
		}
		self.name=name
		self.descr=descr
		self.files=files
		self.md5=md5
		self.status=status
		self.hosts=hosts
		print(hosts)
		self.proj_name=proj_name
		self.cves=cves
		global jira_session
		# print("Trying to authorize")
		os.environ['https_proxy']='http://127.0.0.1:8080'
		os.environ['http_proxy']='http://127.0.0.1:8080'
		self.jira_session = JIRA(basic_auth=(self.config['username'], self.config['password']), options = {'server': 'https://jira.kaspersky.com', 'verify': False, 'validate': False}, proxies={'http': 'http://127.0.0.1:8080','https': 'https://127.0.0.1:8080'}, max_retries=2, timeout=60) #timeout=5
		print(self.jira_session)
		# return jira_session

	def createIssue(self):
		# options = {'verify': False, 'server': 'https://jira.kaspersky.com', 'proxies':self.proxies}
		# jira = JIRA(options=options, basic_auth=(self.config['username'], self.config['password']))
		issue_dict = {
			'project': {'key': 'SOC'},
			'summary': self.name,
			'description': self.descr,
			'customfield_14025': self.hosts,
			'customfield_14026': self.files,
			'customfield_14024': self.cves,
			'customfield_13805': 'Nessus',
			# 'components':[{'name':""}],
			"assignee": {
				"name": "unassigned"
				},
			'issuetype': {'name': 'Incident'}
		}
		new_issue = self.jira_session.create_issue(fields=issue_dict)
		# if len(self.files)>0:
		# 	for file in self.files:
		self.jira_session.add_attachment(issue=new_issue, attachment=self.files)
		return new_issue
	
	def makeItResolved(self,issue):
		self.jira_session.transition_issue(issue, '1st tier investigation') # id = 11
		self.jira_session.transition_issue(issue, 'True Positive', fields={'customfield_14500': 'Report was sent'})
	def makeItOnHold(self,issue):
		self.jira_session.transition_issue(issue, '1st tier investigation') # id = 11
		self.jira_session.transition_issue(issue, 'On Hold', fields={'customfield_14500': self.status})
		# self.jira_session.transition_issue(issue, transition='')
		# self.jira_session.transition_issue(issue, transition='5')

