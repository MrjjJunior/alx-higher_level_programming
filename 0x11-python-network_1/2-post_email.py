#!/usr/bin/python3
''' script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a paramete
    ,and displays the body of the response
    '''

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
