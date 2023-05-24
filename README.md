# code2flow_api

Usage Example:

``` python
import requests

url = 'http://address/upload_script'
file = {'file': open('trader_script.py', 'rb')}
resp = requests.post(url=url, files=file)
print(resp)
```
