#!/usr/bin/python3
'''
Script takes in URL, sends a request to the URL
and displays the value of the X-Request-Id
'''

import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        xRequestId = response.getheader('X-Request-Id')
        print(xRequestId)
