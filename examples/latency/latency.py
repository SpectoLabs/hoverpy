# latency.py

from hoverpy import capture
import requests

delays = [("time.jsontest.com", 3000, "GET"), ("echo.jsontest.com", 1000)]

@capture("delays.db", recordMode="once", delays=delays)
def simulate_network_latency():
    print(requests.get("http://time.jsontest.com").text)
    print(requests.get("http://echo.jsontest.com/a/b").text)

simulate_network_latency()
