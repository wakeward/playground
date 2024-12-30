#!/usr/bin/python3
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u','--user', help='Username to target', required=True)
parser.add_argument('-p','--password', help='Password value to set', required=True)
parser.add_argument('-s', '--server', help='Server IP or Hostname', required=True)
args = parser.parse_args()

auth_endpoint = 'http://{args.server}:8080/v1/auth/login'
# payload = {'username':args.user, 'password':args.password}
headers = {'Content-type': "application/json; charset=utf-8"}

# Create a session object
session = requests.Session()
# Set the auth credentials
session.auth = (args.user, args.password)
# Update the headers
session.headers.update(headers)

# Perform the authentication request
auth = session.post(url=auth_endpoint, auth=(args.user, args.password))
print(auth.text)

# Perform a request to the protected endpoint
r = session.get('http://{args.server}:8080/v1/auth/protected')
print(r.text)