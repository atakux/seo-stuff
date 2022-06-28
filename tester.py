import requests
from requests.auth import HTTPBasicAuth

response = requests.get('http://acnhapi.com/', auth = HTTPBasicAuth('user', 'pass'))

print(response)