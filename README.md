# api-request-counter
API request limit counter

## example
```python
import api_counter as apiCounter
import urllib.request as socket
import urllib.error as urlerr
from urllib.parse import quote

api_url = ""

counter = apiCounter.APIRequestCounter(5, apiCounter.TimeEnum.S)

for i in range(50):
    counter.requestCount(True)
    response = socket.urlopen(api_url)

for i in range(50):
    if counter.requestCount(False) is True:
        response = socket.urlopen(api_url)
    else:
        print("False")
```
