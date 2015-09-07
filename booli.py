import httplib
import time
from hashlib import sha1
import random
import string
import json
from flask import Blueprint, make_response, jsonify, request
from sys import argv

import os

# Get the current directory
current_dir = os.getcwd();
print "Current directory: " + current_dir

#Get the path and name of the file where the output data will be stored 
filename = current_dir + "/data/booli.json" 


callerId = "DataAfterLife"
timestamp = str(int(time.time()))
unique = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(116))
hashstr = sha1(callerId+timestamp+"XQc9CrWSJInMEnGjLnXE85aheCS8DqsFv2N5HXMi"+unique).hexdigest()

url = "/sold?q=karlstad&callerId="+callerId+"&time="+timestamp+"&unique="+unique+"&hash="+hashstr

connection = httplib.HTTPConnection("api.booli.se")
connection.request("GET", url)
response = connection.getresponse()
data = response.read()
connection.close()

if response.status != 200:
    print "fail"

result = data

result_pretty_json = json.loads(result)

# Open the stream to write to a file
target = open(filename, 'w')

target.write(json.dumps(result_pretty_json, indent=4))
#target.write(json.dumps(result_pretty_json, indent=4, sort_keys=True))
#print result