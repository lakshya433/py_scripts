import requests 
import sys 

sub_list = open("PathToYourWordlist").read()                 #open and read wordlist as whole
directories = sub_list.splitlines()                         #split lines and make list

for dir in directories:                                        #go through list
    if sys.srgv[1] != "":
        dir_enum = f"http://{sys.argv[1]}/{dir}"            #url to check
    else:
        print("usage: python3 dir_scan.py example.com")

    r = requests.get(dir_enum)                              #get req to url
    if r.status_code==404:                                  #for 404 error
        pass                                                #ignore and continue script
    else:
        print("Valid directory:" ,dir_enum)                 #when no error print current dir name 