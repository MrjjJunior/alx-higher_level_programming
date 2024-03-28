#!/usr/bin/python3
''' script that fetches URL '''

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = request.get(url)

    body = response.text

    print("Body response:")
    print("    - type:")
    print("    - content:")
