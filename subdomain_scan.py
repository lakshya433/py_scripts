import requests
import sys

list = open("PathToYourWordlist").read()
subdoms = list.splitlines()

for sub in subdoms:
        
        if {sys.argv[1]} != "":
            subdomain = f"http://{sub}.{sys.argv[1]}"
        else:
            print("usage example:  python3 subdomain_scan.py example.com")

        try:
                requests.get(subdomain)
        except requests.ConnectionError:
                pass


        else:
                print("valid domain: ",subdomain)
