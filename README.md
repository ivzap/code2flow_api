# code2flow_api

Usage Examples:

File Version:
``` python
import requests

url = 'http://address/upload_script'
file = {'file': open('trader_script.py', 'rb')}
resp = requests.post(url=url, files=file)
print(resp)
```

String Version:
``` python
url = 'http://k-20014:8000/upload_script'
with open('test1.py', 'r') as f:
    raw = f.read()
param = {'script': raw}
resp = requests.post(url=url, json=param)
print(resp)
with open('response.html', 'w') as f:
    f.write(resp.json()['html'])
```
