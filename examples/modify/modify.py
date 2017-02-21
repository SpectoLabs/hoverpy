import requests
from hoverpy import modify

@modify(middleware="python examples/modify/middleware.py")
def get_modified_time():
    print(requests.get("http://time.ioloop.io?format=json").json())

get_modified_time()