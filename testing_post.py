import requests
import json

url = 'http://ipstats.globalcrossing.net/cgi-bin/lg/lg.cgi?lgCall=r2htrace'
payload = {'lgCall': 'r2htrace', 'source':'119637', 'destAddress':'216.58.192.68'}

#headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload))
print(r.status_code, r.reason)
print(r.text)
