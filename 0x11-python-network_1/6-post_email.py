#!/usr/bin/python3
'''
Script takes in a URL and an email address,
sends a POST request to the passed URL
'''

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print("Your email is:", email)
    print(response.text)
