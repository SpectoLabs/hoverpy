from hoverpy import capture
import requests
import time

@capture("readthedocs.db", recordMode="once")
def getLinks(limit):
    start = time.time()
    sites = requests.get(
        "http://readthedocs.org/api/v1/project/?limit=%d&offset=0&format=json" % int(limit))
    objects = sites.json()['objects']

    for link in ["http://readthedocs.org" + x['resource_uri'] for x in objects]:
        response = requests.get(link)
        print("url: %s, status code: %s" % (link, response.status_code))

    print("Time taken: %f" % (time.time() - start))

getLinks(50)