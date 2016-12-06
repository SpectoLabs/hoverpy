#!/usr/bin/python

from hoverpy import HoverPy
import pysimplesoap
import requests

from argparse import ArgumentParser

parser = ArgumentParser(description="Perform proxy testing/URL list creation")
parser.add_argument("--capture", help="capture the data", action="store_true")
args = parser.parse_args()


with HoverPy(capture=args.capture):
    ipAddress = requests.get("http://ip.jsontest.com/myip").json()["ip"]
    pysimplesoap.transport.set_http_wrapper("urllib2")

    client = pysimplesoap.client.SoapClient(
        wsdl='http://ws.cdyne.com/ip2geo/ip2geo.asmx?WSDL'
    )

    print(client.ResolveIP(ipAddress=ipAddress, licenseKey="0"))
