Import hoverpy's main class: HoverPy 

```python
from hoverpy import HoverPy

```

Import requests and random for http and testing 

```python
import requests
import random

```

Create our HoverPy object in capture mode 

```python
hp = HoverPy(capture=True)

```

This function either generates a echo server url, or a md5 url it is seeded so that we get the exact same requests on capture as we do on simulate 

```python
def getServiceData():
  for i in range(10):
    random.seed(i)
    print(requests.get(random.choice(["http://echo.jsontest.com/i/%i"%i, "http://md5.jsontest.com/?text=%i"%i])).json())

```

Make the requests to the desired host dependencies 

```python
print("capturing responses from echo server\n")
getServiceData()

```

There are two ways to add delays. One is to call the delays method with the desired delay rules passed in as a json document  

```python
print hp.delays({"data":[
                    {
                      "urlPattern": "md5.jsontest.com",
                      "delay": 1000
                    }
                  ]
                }
              )

```

The other more pythonic way is to call addDelay(...) 

```python
print hp.addDelay(urlPattern="echo.jsontest.com", delay=3000)

```

Now let's switch over to simulate mode 

```python
print hp.simulate()

```

Make the requests. This time HoverFly adds the simulated delays. these requests would normally be run asynchronously, and we could deal gracefully with the dependency taking too long to respond 

```python
print("\nreplaying delayed responses from echo server\n")
getServiceData(

```

