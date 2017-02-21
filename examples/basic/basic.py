from hoverpy import capture, simulate
import requests

@capture("requests.db")
def captured_get():
    print(requests.get("http://time.jsontest.com").json())

@simulate("requests.db")
def simulated_get():
    print(requests.get("http://time.jsontest.com").json())

captured_get()
simulated_get()