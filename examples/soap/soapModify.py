#!/usr/bin/python

from hoverpy import HoverPy
import pysimplesoap
import requests

with HoverPy(modify=True, middleware="python examples/soap/modify_payload.py"):
    ipAddress = requests.get("http://ip.jsontest.com/myip").json()["ip"]
    pysimplesoap.transport.set_http_wrapper("urllib2")

    client = pysimplesoap.client.SoapClient(
        wsdl='http://ws.cdyne.com/ip2geo/ip2geo.asmx?WSDL'
    )

    print(client.ResolveIP(ipAddress=ipAddress, licenseKey="0"))
