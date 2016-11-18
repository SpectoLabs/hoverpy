Import hoverpy's main class: HoverPy 

```python
from hoverpy import HoverPy

```

Import requests and random for http 

```python
import requests

```

Create our HoverPy object in capture mode 

```python
hp = HoverPy(capture=True)

```

Print the json from our get request. Hoverpy acted as a proxy: it made the request on our behalf, captured it, and returned it to us. 

```python
print(requests.get("http://ip.jsontest.com/myip").json())

```

Switch HoverPy to simulate mode. HoverPy no longer acts as a proxy; all it does from now on is replay the captured data. 

```python
hp.simulate()

```

Print the json from our get request. This time the data comes from the store. 

```python
print(requests.get("http://ip.jsontest.com/myip").json())

```

