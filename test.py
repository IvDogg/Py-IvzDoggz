#0 
#'POINTS:1,TIMED:Y - The data element contains a string comprised of two integers separated by a space.   Add them together and submit the sum.'

data0 = '93 841'

game.answer(0, sum(map(int, game.data(0).split())))

#1
#'POINTS:1,TIMED:Y - The data element contains a long string.  Extract the substring that is surounded by dashes.  Submit that substring.'
data1 = 'kSgYZqeUtlrnBFxoWDNaiTIfCLXJGKA-See an old lady walking down the street.  Laptop on hand with >>> on the screen.-pyFzhJAdBWixCOmlkvYcKnsatXfePIq'

game.answer(1, game.data(1).split("-")[1])

#2
#'POINTS:1,TIMED:Y - Return the 2nd word in the sentence in reverse.   Example "The quick brown cow." would be "kciuq"  '

data2 = 'There is only 0b10 types of people.  Those that understand python and those that dont'

game.answer(2, game.data(2).split()[1][::-1])

#3
#'POINTS:1,TIMED:Y - Base64 decode the string and submit the answer.    '

data3 = 'WW91ciBweXRob24gd2FzIGhvbWUgd2hlbiB5b3UgbGVmdC4gIFlvdXIgcmlnaHQu'

game.answer(3, base64.b64decode(game.data(3)))

#4
#'POINTS:1,TIMED:Y - The data contains a string of numbers separated by commas.   Add together all the numbers and submit the total.'

data4 = '629039,529222,740665,20048,200431,366912,310148,972792,891676,455549,878336,68018,80126,535953,304045,860879,926183,925033,379365,267958,896356,916665,681969,772016,549108,156369,208814,207114,603255,130086,492630,825534,29937,196743,104250,555181,426742,465178,279060,947659,869036,275517,184141,173967,431748,568974,874415,661522,567214,994316'

game.answer(4, sum(map(int, game.data(4).split(","))))

#5
#'POINTS:1,TIMED:Y - Cut the string in half and submit the 2nd half.  Example: "Hello World" would be " World" '

data5 = 'Python Ranger gonna take a little trip'

d = game.data(5); game.answer(5,  d[len(d)/2:])

#6 
#'POINTS:1,TIMED:Y - Convert the base16 string to a decimal number  Example: "0xFF" would be 255 '

d = '0x1add'

game.answer(6, int(game.data(6)[2:6], 16))

#7 
#'POINTS:1,TIMED:Y - The data contains a list. What is the 3rd item in the list? '

d = [991053, 466307, 24600, 527488, 325783, 920756, 576270]

game.answer(7, game.data(7)[2])

#8 
#'POINTS:1,TIMED:Y - The data contains a dictionary. What is the value in the entry with a key of "cyber"?'

d = {'all': 865039, '255s': 805971, 'army': 275714, 'of': 698705, 'cyber': 57702, 'rock': 137597}

game.answer(8, game.data(8)['cyber'])

#9 
#'POINTS:1,TIMED:Y - It is currently 2130 hours.   The data element contains how many hours are left on your shift as towel handler at gym #5.   What time will it be when your shift ends.  Express your answer in proper military time.  Example: 0130  '

d = 43 

game.answer(9, "%02d30" % ((game.data(9) + 21) % 24,))

#10 
#'POINTS:1,TIMED:Y - The data contains your current driving speed and an excuse.   The speed limit is 15 MPH on post and you just got pulled over.\nIf you are not speeding there is no fine.  If your speed is less than 5 MPH over the limit then you are fined $20.00.  If your speed is 5 MPH or more over the limit you are fined $40.00.    However you can try various excuses on the MPs.  If your excuse is "I work at the NSA" no adjustment to the fine is made.   If your excuse is "I work at signal towers" your fine is doubled.  If your excuse is "I am headed to the hospital" no fine is issued.   Any other excuse cuts the fine in half.  Submit the fine as an integer (No Dollar signs, no decimal points). '

d = '24,I am headed to the hospital'

def doanswer10(d):
	speed = int(d.split(",")[0])
	dest = d.split(",")[1]
	fine = 0
	if speed <= 15:
		return fine
	elif speed <= 20:
		fine = 20
		if dest == 'I work at the NSA':
			return fine
		elif dest == 'I work at signal towers':
			return fine * 2
		elif dest == 'I am headed to the hospital':
			return 0
		else:
			return fine
	elif speed > 20:
		fine = 40
		if dest == 'I work at the NSA':
			return fine
		elif dest == 'I work at signal towers':
			return fine * 2
		elif dest == 'I am headed to the hospital':
			return 0
		else:
			return fine

game.answer(10, doanswer10(game.data(10)))

#11
#'POINTS:1,TIMED:Y - Add together all of the unique numbers in the string.  If a number is not unique do not include it in the total.  Example: 1,1,2,3,4,4 would be 5.'

d = '7,9,9,5,9,9,1,0,2'

def doanswer11(d):
	a = []
	d = map(int, d.split(","))
	[a.append(i) for i in d if d.count(i) == 1]
	return sum(a)

game.answer(11, doanswer11(game.data(11)))
	
#12
#'POINTS:1,TIMED:Y - If you are flying Delta airlines and it is raining your flight will be delayed.  If you are in Atlanta GA, your flight will be delayed regardless of weather.   The data element contains your airline, the weather and your location.  Return "delayed" or "not-delayed".   '

d = 'Delta,sunny,Charlotte'

def doanswer12(d):
	airline = d.split(",")[0]
	weather = d.split(",")[1]
	airport = d.split(",")[2]
	if airport == "Atlanta":
		return "delayed"
	elif airline == "Delta":
		if weather == "raining":
			return "delayed"
		else:
			return "not-delayed"
	else:
		return "not-delayed"
		
game.answer(12, doanswer12(game.data(12)))