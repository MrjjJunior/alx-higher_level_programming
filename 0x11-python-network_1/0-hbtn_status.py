#!/usr/bin/python3

from urllib.request import urlopen

with urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()
    utf8 = body.decode('utf-8')


print("Body response:")
print("    - type:", type(body))
print("    -content", body)
print("    - utf8 content:", utf8)
#print(body[:15])