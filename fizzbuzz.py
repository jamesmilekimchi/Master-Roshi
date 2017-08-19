
#for fizzbuzz in range(1,101):
#  if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#    print "FizzBuzz"
#  elif fizzbuzz % 3 == 0:
#    print "Fizz"
#  elif fizzbuzz % 5 == 0:
#    print "Buzz"
#  else:
#    print fizzbuzz

oxford = {}
oxford['3'] = "Fizz"
oxford['5'] = "Buzz"
oxford['7'] = "Wizz"
oxford['11'] = "Duzz"

for fizzbuzz in range(1,1156):
	output = ''

	for key in oxford.keys():
		if fizzbuzz % int(key) == 0:
			output += str(oxford[key])
	
	if output == '':
		output = str(fizzbuzz)
	print output
