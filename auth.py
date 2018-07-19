from __future__ import print_function
import httplib2
import os
import base64
import email
from email.mime.text import MIMEText
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
 
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


class auth:
	def_init_(self,SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME):
    	self.SCOPES=SCOPES
    	self.CLIENT_SECRET_FILE=CLIENT_SECRET_FILE
    	self.APPLICATION_NAME=APPLICATION_NAME
	def get_credientials(self):
	    cwd_dir = os.getcwd()
        credential_dir = os.path.join(cwd_dir, '.credentials')
	    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    	credential_path = os.path.join(credential_dir,
                                             'gmail-python-quickstart.json')
 
    	store = oauth2client.file.Storage(credential_path)
    	credentials = store.get()
    	if not credentials or credentials.invalid:
        	flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
        if flags:
             credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
             credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


