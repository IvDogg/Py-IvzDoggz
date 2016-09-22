import itertools
import string
chars = string.digits
FILE = open("w2.txt","w")
for xs in itertools.product(chars, repeat=6):
	print '#'+''.join(xs)+'#'
	FILE.write('#'+''.join(xs)+'#\n')
