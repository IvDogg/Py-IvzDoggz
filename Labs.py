#XORG
payload = "\x0B\x0D\xFF\xAF"
key = "ABCD"

encrypted_text = ""

for position, char in enumberate(key):
	encrypted_text = encrypted_text + chr(ord(char) ^ ord(payload[position]))
	
#MilitaryTime

x = 25
(x + 21) % 24
22

"%02d30" % ((x+21) % 24,)

#Half

x[len(x)/2:]

#HEX String to Decimal

x = "0xc8a"

int(x, 16)

#unique



#1
game.answer(1, game.data(1)+5)

#2

import string
rot13 = string.maketrans( 
     "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
     "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
string.translate(game.data(2), rot13)

game.answer(2, string.translate(game.data(2), rot13))

#3

import base64
base64.b64decode(game.data(3))
'The Knights Who Say Ni'
game.answer(3,base64.b64decode(game.data(3)))

#4

game.answer(4,game.data(4).upper())

#5

game.answer(5,game.data(5).index('SANS'))

#6

game.answer(6,game.data(6)[::-1])

#7

data7=game.data(7)
game.answer(7,data7+data7[::-1]+data7)

#8

data8=game.data(8)
game.answer(8,data8[1]+data8[4]+data8[8])

#9

#'Swap the first and last character. For example frog->grof, Hello World->dello Worlh etc. '
data9=game.data(9)
game.answer(9, data9[-1] + data9[1:-1] + data9[0])

#10
#'Reverse the first half of the data(). For example sandwich->dnaswich '
data10=game.data(10)
game.answer(10, data10[:len(data10) // 2][::-1] + data10[len(data10) // 2:])

#11
#'Leet speak it (E->3,A->4,T->7,S->5,G->6) convert only uppercase letters. For example LeEtSpEAk->Le3t5p34k '

game.answer(11, game.data(11).replace("E","3").replace("A","4").replace("T","7").replace("S","5").replace("G","6"))

#12
#'Read the list from data and return the 3rd element '

game.answer(12, list(game.data(12))[2])

#13
#'Build a list of numbers starting at 1 and up to but not including the number in data(). '

def countUp(end):
     i = 1
     while i < end:
             print i
             i = i + 1
			 
def countUp(end):
     i = 1
     numbers = []
     while i < end:
             print "adding " + str(i) + "to list"
             numbers.append(i)
             i = i + 1
     list(numbers)
	 
def countUp(end):
     i = 1
     numbers = []
     while i < end:
             numbers.append(i)
             i = i + 1
     print numbers
	 
game.answer(13, range(1,game.data(13),1))
	 
#14
#'Count the number of items in the list in data().  The answer is the number of items in the list.'

game.answer(14, len(game.data(14)))

#15
#'Split the data element based on the comma (",") delimiter and return the 10th element '

game.answer(15, game.data(15).split(',')[9])

#16
#'The data element contains a line from an /etc/shadow file. The shadow file is a colon delimited file.  The 2nd field in the colon delimited field contains the password information.   The password information is a dollar sign delimited field with three parts.  The first part indicates what cypher is used.  The second part is the password salt.  The last part is the password hash.   Retrieve the password salt for the root user.'

game.answer(16, game.data(16).split(':')[1].split('$')[2])

#17
#'Add a string of "Pywars rocks" to the end of the list in the data element.  Submit the new list. '

def addtolist(data17):
     data17.append('Pywars rocks')
     return data17
	 
game.answer(17, addtolist(game.data(17)))

#18
#'Add up all the numbers in the list and submit the total. '

game.answer(18, sum(game.data(18)))

#19
#'Given a string that contains numbers separated by spaces, add up the numbers and submit the sum.  "1 1 1" -> 3 '

game.answer(19, sum(map(int, game.data(19).split(' '))))

#20
#'Create a string by joining together the words "this","python","stuff","really","is","fun" by the character in .data().   For example if data contains a hyphen (ie "-") then you submit "this-python-stuff-really-is-fun".  '

data20 = game.data(20); answer20 = "this" + data20 + "python" + data20 + "stuff" + data20 + "really" + data20 + "is" + data20 + "fun"; game.answer(20, answer20)

#21
#'The answer is the list of numbers between 1 and 1000 that are evenly divisible by the number provided.  2->[2,4,6,8..] 4->[4,8,16..] '

def dividelist(data21):
	i = int(1)
	list = []
	while i < 1001:
		if i % data21 == 0:
			list.append(i)
		i = i + 1
	return list
game.answer(21, dividelist(game.data(21)))

#22
#'Given a list of hexadecimal digits return a string that is made from their ASCII characters.  Ex [41 4f] -> "AO" '

def hexconv(data22):
	i = ""
	s = ""
	for i in data22:
		s += chr(int(i, 16))
	return s
	
game.answer(22, hexconv(game.data(22)))

#23
#'You will be given a list that contains two lists.  Combine the two lists and eliminate duplicates.  The answer is the SORTED combined list.  [[d,b,a,c][b,d]] -> [a,b,c,d] '

def combinelist(data23):
	x = data23[0]
	y = data23[1]
	for y in x:
		if y not in x:
			x.append(y)
	return sorted(x)
	
def combinelist(data23):
	uniquelist = []
	for item in data23[0]+data23[1]:
		if not item in uniquelist:
			uniquelist.append(item)
	return sorted(uniquelist)
	
game.answer(23, combinelist(game.data(23)))

#24
#'Sort the elements in the list in numerical order.  Submit the sorted list. '

game.answer(24, sorted(game.data(24)))

#25
#'Data contains a list of comma separated numbers.   If the second number is evenly divisible by the first return TRUE in a list at the same index.  If it is not evenly divisible return false.  For example [ "6,36" , "2,8" , "3,11" ] you would answer [ "True" , "True", "False" ] because  36 is evenly divisible by 6, 8 is evenly divisible by 2 and 11 is NOT evenly divisble by 3.  Note the responses are case sensitive strings of either "True" or "False". '

for item in data25:
	a = item.split("'")
	b = a[0].split(",")
	if int(b[1]) % int(b[0]) == 0:
		s += "\"True\", "
	else:
		s += "\"False\", "
	s[:-2]

def divideby(data25):
	s = ""
	for item in data25:
		a = item.split("'")
		b = a[0].split(",")
		if int (b[1]) % int(b[0]) == 0:
			s += "\"True\", "
		else:
			s += "\"False\", "
	return s[:-2]
	
def do25(data):
	true_false_list = []
	for pair in data:
		first_int = int(pair.split(",")[0])
		second_int = int(pair.split(",")[1])
		if (second_int % first_int) == 0:
			true_false_list.append("True")
		else:
			true_false_list.append("False")
	return true_false_list

game.answer(25, do25(game.data(25)))

#26
#'Data contains a list of objects.  The answer is a list that contains the type of each of these elements.  Create a list that contains the type of each element in the list provided. '

data26 = [[1, 1], '1', {1: 1}, {1: 1}, 1.1, 1.1, 1, [1, 1], [1, 1], '1', 1, 1.1, [1, 1], 1, 1]

for item in data26:
	m.append(str(type(item))[7:-2])
	
for item in data26:
	str(type(item))[7:-2]
	
def typelist(data26):
	m = []
	for item in data26:
		m.append(str(type(item))[7:-2])
	return m
	
game.answer(26, [type(y) for y in x])


#27
#'Data contains a dictionary.  Submit a SORTED list of all of the keys in the dictionary. '

data27 = {'6': 'b', '8': '6', 'e': 's', 'i': 'e', 'h': 'e', 'j': 'j', 'm': 'l', 'l': '9', 'p': 'h', '3': 'w', 'u': 'q', '4': '7', 'v': 'i', '5': 'p'}

game.answer(27, sorted(game.data(27)))

#28
#'Data contains a dictionary.  Submit a SORTED list of all of the values in the dictionary.'

data28 = {'7': 'y', 'c': '3', 'e': 'e', 'f': 's', 'j': '9', 'n': 'q', '3': 'd', 'u': 't', '4': 'p', 'w': 'e', 'y': 'l', 'x': 'i'}

game.answer(28, sorted(game.data(28).values()))

#29
#'Data contains a dictionary.  Submit a SORTED list of tuples.  There should be one tuple for each entry in the dictionary. Each tuple should contain a key and its associated value from the dictionary.'

data29 = {'w': 'f', 'i': 'g', 'h': 's', '3': 'p', '1': 'd', 's': 'd', 'r': 'j', '5': '3', '7': '8', 'v': 'v', '9': 'n', '8': '6'}

game.answer(29, sorted(game.data(29).items()))

#30
#'Data contains a dictionary.  Add together the integers stored in the dictionary entries with the keys "python" and "rocks" and submit their sum. '

data30 = {'python': 592, 'big': 40, 'rocks': 589}

data30 = game.data(30); game.answer(30, data30['python'] + data30['rocks'])

#31
#"Data contains a dictionary of dictionaries.  The outer dictionary contains dates in the format of Month-Year.  The value for each of those entries is another dictionary.  That dictionary contains Operating System classes as they key and its percentage of use in the target organization as the value.  What percentage of the attack surface was 'Vista' in '6-2013'?"

data31 = {'11-2013': {'Vista': '0.25', 'WinXP': '0.09', 'Mobile': '0.27', 'Win7': '0.43', 'Mac': '0.02', 'NT*': '0.06', 'Linux': '0.18'}, '6-2013': {'Vista': '0.25', 'WinXP': '0.08', 'Mobile': '0.22', 'Win7': '0.44', 'Mac': '0.06', 'NT*': '0.09', 'Linux': '0.18'}, '8-2013': {'Vista': '0.29', 'WinXP': '0.08', 'Mobile': '0.23', 'Win7': '0.48', 'Mac': '0.06', 'NT*': '0.05', 'Linux': '0.12'}, '5-2013': {'Vista': '0.28', 'WinXP': '0.09', 'Mobile': '0.2', 'Win7': '0.42', 'Mac': '0.04', 'NT*': '0.05', 'Linux': '0.16'}, '7-2013': {'Vista': '0.26', 'WinXP': '0.09', 'Mobile': '0.24', 'Win7': '0.45', 'Mac': '0.06', 'NT*': '0.09', 'Linux': '0.16'}, '3-2013': {'Vista': '0.27', 'WinXP': '0.09', 'Mobile': '0.26', 'Win7': '0.4', 'Mac': '0.04', 'NT*': '0.08', 'Linux': '0.11'}, '4-2013': {'Vista': '0.29', 'WinXP': '0.05', 'Mobile': '0.29', 'Win7': '0.42', 'Mac': '0.07', 'NT*': '0.02', 'Linux': '0.17'}, '1-2013': {'Vista': '0.26', 'WinXP': '0.09', 'Mobile': '0.27', 'Win7': '0.42', 'Mac': '0.02', 'NT*': '0.03', 'Linux': '0.1'}, '9-2013': {'Vista': '0.21', 'WinXP': '0.09', 'Mobile': '0.22', 'Win7': '0.41', 'Mac': '0.06', 'NT*': '0.07', 'Linux': '0.14'}, '10-2013': {'Vista': '0.29', 'WinXP': '0.06', 'Mobile': '0.24', 'Win7': '0.48', 'Mac': '0.06', 'NT*': '0.02', 'Linux': '0.14'}, '2-2013': {'Vista': '0.2', 'WinXP': '0.06', 'Mobile': '0.21', 'Win7': '0.46', 'Mac': '0.03', 'NT*': '0.05', 'Linux': '0.11'}, '12-2013': {'Vista': '0.23', 'WinXP': '0.09', 'Mobile': '0.26', 'Win7': '0.41', 'Mac': '0.06', 'NT*': '0.08', 'Linux': '0.16'}}

game.answer(31, game.data(31)['6-2013']['Vista'])

#32
#'Data contains a dictionary of dictionaries.  The outer dictionary contains dates in the format of Month-Year.  The value for each of those entries is another dictionary.  That dictionary contains Operating System classes as they key and its percentage of use in the target organization as the value.  You have an exploit that will work against XP, NT and VISTA.  What month had the most vulnerable targets?  IE Add up the percentage for XP, NT and Vista.  Submit the month (1,2,3,4,5,6,7,8,9,10,11 or 12) that has the highest percentage. If two months have the same percentage submit the most recent.'

data32 = {'11-2013': {'Vista': '0.27', 'WinXP': '0.08', 'Mobile': '0.2', 'Win7': '0.44', 'Mac': '0.05', 'NT*': '0.06', 'Linux': '0.16'}, '6-2013': {'Vista': '0.23', 'WinXP': '0.06', 'Mobile': '0.28', 'Win7': '0.46', 'Mac': '0.07', 'NT*': '0.05', 'Linux': '0.17'}, '8-2013': {'Vista': '0.22', 'WinXP': '0.09', 'Mobile': '0.26', 'Win7': '0.49', 'Mac': '0.09', 'NT*': '0.07', 'Linux': '0.12'}, '5-2013': {'Vista': '0.27', 'WinXP': '0.08', 'Mobile': '0.23', 'Win7': '0.47', 'Mac': '0.04', 'NT*': '0.04', 'Linux': '0.11'}, '7-2013': {'Vista': '0.26', 'WinXP': '0.06', 'Mobile': '0.27', 'Win7': '0.47', 'Mac': '0.08', 'NT*': '0.07', 'Linux': '0.11'}, '3-2013': {'Vista': '0.28', 'WinXP': '0.07', 'Mobile': '0.29', 'Win7': '0.41', 'Mac': '0.04', 'NT*': '0.04', 'Linux': '0.15'}, '4-2013': {'Vista': '0.29', 'WinXP': '0.08', 'Mobile': '0.21', 'Win7': '0.49', 'Mac': '0.08', 'NT*': '0.07', 'Linux': '0.11'}, '1-2013': {'Vista': '0.2', 'WinXP': '0.09', 'Mobile': '0.25', 'Win7': '0.42', 'Mac': '0.02', 'NT*': '0.03', 'Linux': '0.18'}, '9-2013': {'Vista': '0.2', 'WinXP': '0.07', 'Mobile': '0.29', 'Win7': '0.4', 'Mac': '0.04', 'NT*': '0.09', 'Linux': '0.13'}, '10-2013': {'Vista': '0.27', 'WinXP': '0.08', 'Mobile': '0.29', 'Win7': '0.45', 'Mac': '0.05', 'NT*': '0.05', 'Linux': '0.16'}, '2-2013': {'Vista': '0.23', 'WinXP': '0.06', 'Mobile': '0.24', 'Win7': '0.46', 'Mac': '0.03', 'NT*': '0.03', 'Linux': '0.16'}, '12-2013': {'Vista': '0.29', 'WinXP': '0.09', 'Mobile': '0.26', 'Win7': '0.48', 'Mac': '0.05', 'NT*': '0.09', 'Linux': '0.11'}}

def answer32(data32):
	highest = 0
	highmonth = ""
	for mon in sorted(data32.keys(), key=lambda x:int(x.split('-')[0])):
		tot = float(data32[mon]['NT*'])+float(data32[mon]['WinXP'])+float(data32[mon]['Vista'])
		if tot>=highest:
			highmonth=mon
			highest=tot
	return highmonth.split("-")[0]
		
game.answer(32, answer32(game.data(32)))

#33
#'Data contains a comma separated list of usernames and passwords in the format user1:password1, user2:password2, etc.   One of those passwords is the answer.  Guess which one. '

data33 = 'Aiden : 123456 , Jayden : porsche , Max : firebird , Riley : prince , Liam : rosebud , Ethan : password , Jack : guitar , Avery : butter , Dylan : beach , Caleb : jaguar , Addison : 12345678 , James : chelsea , Ryan : united , Andrew : froggy , NavajoElla : great , Ava : 1234 , Grace : black , Limabean : turtle , Emma : 7777777 , Elizabeth : cool , Genevieve : puddy , Aurora : diamond , Isabella : steelers , Bella : muffin , Charlotte : cooper '



