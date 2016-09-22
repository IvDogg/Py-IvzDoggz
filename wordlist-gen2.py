#! C:\python27

import string, random

#============ Word List Gen ============
minimum=8
maximum=8
wmaximum=10000

#alphabet = string.letters[0:52] + string.digits + string.punctuation
alphabet = string.digits
string=''
FILE = open("wl.txt","w")
for count in xrange(0,wmaximum):
	for x in random.sample(alphabet,random.randint(minimum,maximum)):
		string+=x
		FILE.write('#'+string+'#\n')
		string=''
		FILE.close()
		print 'DONE!'

#============    WLG END    ============