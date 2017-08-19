# Project Master Roshi
## Day 5
Things I learnt:

- Modulo Operation

[In computing, the modulo operation finds the remainder after division of one number by another (sometimes called modulus).](https://en.wikipedia.org/wiki/Modulo_operation)

1. It works with the "%" sign
2. Number After "%" checks if numbers can be divisible by the Number
``` python

if number % 3 == 0:
	print "divisible by 3"

```
## My task of the day
### __The Fizzbuzz sequence__
The rule is that I have to display the first hundred number but put a "Fizz" when the number is a factor of 3, a "buzz" if a factor of 5 and a fizzbuzz if both.

``` python

for fizzbuzz in range(1,101):
  if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print "FizzBuzz"
  elif fizzbuzz % 3 == 0:
    print "Fizz"
  elif fizzbuzz % 5 == 0:
    print "Buzz"
  else:
    print fizzbuzz

```

## Bonus!!!
### Use a dictionary for fizzbuzz

```python
oxford = {}
oxford['3'] = "Fizz"
oxford['5'] = "Buzz"


for fizzbuzz in range(1,1156):
	output = ''

	for key in oxford.keys():
		if fizzbuzz % int(key) == 0:
			output += str(oxford[key])
	
	if output == '':
		output = str(fizzbuzz)
	print output

```
- The second program just does the same thing but just works with the dictionary instead of If and elses.
- The Benefits:
1. Easier to __interpret__ the program by look. Programs are for human!! So must be readable.
2. It is way __shorter__.Less Codes there are, less mistakes you can make.
3. __Update information__ (key/value) faster. Just has to change once at the dictionary.
4. The dictionary works __faster__ than many if and else. 
[“In the worst case scenario I created for the IF statement logic, it’s 18 times slower than the method using a dictionary.  We can do that again with more complex strings”]( http://scottlobdell.me/2014/05/time-efficiency-statements-vs-python-dictionaries/)
5. __And __[Master Roshi](https://github.com/shinroo/)__ said so!__

I just passed a __common software engineer position test!__

__Thank you Master Roshi!__

__Follow this GOAT for amazing softwares!!!__

[https://github.com/shinroo/](https://github.com/shinroo/)
 
