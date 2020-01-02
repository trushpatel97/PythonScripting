#You will not be able to run this file here and will need to copy it onto your computer and run it on your machine. 
#You will also need to make sure you have installed the requests module from PyPi (pip install)
import requests
import sys
import json

url = 'https://haveibeenpwned.com/api/v3/breaches'
response= requests.get(url)

def jprint(obj):
	text = json.dumps(obj,sort_keys=True, indent=4)
	print(text)
result = jprint(response.json())

for item in range(len(result)):
	for key in dataList[index]:
		print(dataList[index][key])
