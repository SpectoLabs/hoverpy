Import hoverpy's main class: HoverPy 

```python
from hoverpy import HoverPy

```

Create our HoverPy object in capture mode 

```python
hp = HoverPy(capture=True)

```

Import urllib3 for http, and build a proxy manager 

```python
import urllib3
http = urllib3.proxy_from_url("http://localhost:8500/")

```

Print the json from our get request. Hoverpy acted as a proxy: it made the request on our behalf, captured it, and returned it to us. 

```python
print(http.request('GET', 'http://ip.jsontest.com/myip').data)

```

Switch HoverPy to simulate mode. HoverPy no longer acts as a proxy; all it does from now on is replay the captured data. 

```python
hp.simulate()

```

Print the json from our get request. This time the data comes from the store. 

```python
print(http.request('GET', 'http://ip.jsontest.com/myip').data)

```

