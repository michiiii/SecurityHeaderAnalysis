#!/bin/python3

# as base we need the cleaned up results of shcheck.py using all webservices in scope
##### shcheck.py -d -g -j -k --hfile webservices.txt > header_check_new.json

import json 

jsonfile="header_check_new.json"
# Opening JSON file
f = open(jsonfile)
  
# returns JSON object as 
# a dictionary
data = json.load(f)


# Initialize Arrays
MISSING_CONTENT_TYPES_ARRAY=[]
MISSING_HSTS_ARRAY=[]
MISSING_XFRAME_ARRAY=[]
MISSING_REFERER_ARRAY=[]
MISSING_PERMISSIONS_ARRAY=[]
MISSING_CSP_ARRAY=[]


# Iterating through the json
# list
for url_object in data:
    url=url_object
    url_missing_arr=data[url]["missing"]

    if "Strict-Transport-Security" in url_missing_arr:
        MISSING_HSTS_ARRAY.append(url)
    if "X-Frame-Options" in url_missing_arr:
        MISSING_XFRAME_ARRAY.append(url)
    if "X-Content-Type-Options" in url_missing_arr:
        MISSING_CONTENT_TYPES_ARRAY.append(url)
    if "Referrer-Policy" in url_missing_arr:
        MISSING_REFERER_ARRAY.append(url)
    if "Permissions-Policy" in url_missing_arr:
        MISSING_PERMISSIONS_ARRAY.append(url)
    if "Content-Security-Policy" in url_missing_arr:
        MISSING_CSP_ARRAY.append(url)

### Sort the arrays
MISSING_CONTENT_TYPES_ARRAY.sort()
MISSING_HSTS_ARRAY.sort()
MISSING_XFRAME_ARRAY.sort()
MISSING_REFERER_ARRAY.sort()
MISSING_PERMISSIONS_ARRAY.sort()
MISSING_CSP_ARRAY.sort()



print("===================================================")
print("============== Missing Strict-Transport-Security")
print("===================================================")
print(*MISSING_HSTS_ARRAY, sep ="\n")
print("\n\n")
print("===================================================")
print("============== Missing X-Frame-Options")
print("===================================================")
print(*MISSING_XFRAME_ARRAY, sep ="\n")
print("\n\n")
print("===================================================")
print("============== Missing X-Content-Type-Options")
print("===================================================")
print(*MISSING_CONTENT_TYPES_ARRAY, sep ="\n")
print("\n\n")
print("===================================================")
print("============== Referrer-Policy")
print("===================================================")
print(*MISSING_REFERER_ARRAY, sep ="\n")
print("\n\n")
print("===================================================")
print("============== Content-Security-Policy")
print("===================================================")
print(*MISSING_CSP_ARRAY, sep ="\n")
print("\n\n")
print("===================================================")
print("============== Permissions-Policy")
print("===================================================")
print(*MISSING_PERMISSIONS_ARRAY, sep ="\n")
print("\n\n")


# Closing file
f.close()
