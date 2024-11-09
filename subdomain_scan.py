import requests
import sys

list = open("PathToYourWordlist").read()              #read wordlist
subdoms = list.splitlines()                           #make list

for sub in subdoms:
        
        if {sys.argv[1]} != "":
            subdomain = f"http://{sub}.{sys.argv[1]}"   #subdomain.url formatting
        else:
            print("usage example:  python3 subdomain_scan.py example.com")

        try:
                requests.get(subdomain)             #make get request
        except requests.ConnectionError:            #for error pass
                pass

        else:
                print("valid domain: ",subdomain)   #print valid domain
