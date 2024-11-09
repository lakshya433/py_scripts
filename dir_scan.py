import requests 
import sys 

sub_list = open("PathToYourWordlist").read() 
directories = sub_list.splitlines()

for dir in directories:
    if sys.srgv[1] != "":
        dir_enum = f"http://{sys.argv[1]}/{dir}" 
    else:
        print("usage: python3 dir_scan.py example.com")

    r = requests.get(dir_enum)
    if r.status_code==404: 
        pass
    else:
        print("Valid directory:" ,dir_enum)