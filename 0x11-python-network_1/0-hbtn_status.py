#!/usr/bin/python3
""" python script that fetches an url and prints response body """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
