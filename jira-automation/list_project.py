# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://---------------.atlassian.net/rest/api/3/project"

API_TOKEN = ""

auth = HTTPBasicAuth("nitheeshrajkm23@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output [0]["name"]

print(name)