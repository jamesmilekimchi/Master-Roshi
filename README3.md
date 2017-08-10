# Project Master Roshi
## Day 3
Things I learnt:

- # Making Variables

[A variable is something that holds a value that may change\. In simplest terms, a variable is just a box that you can put stuff in\. You can use variables to store all kinds of stuff\.](https://en.wikibooks.org/wiki/Python_Programming/Variables_and_Strings)

``` python 

Unit = ''
Number = 0

```

- (sys.agrv[])

[It is operating system dependent whether this is a full pathname or not](https://docs.python.org/2/library/sys.html)

1. Goes in order: 0,1,2 etc
2. len(sys.argv) means number of parameter
3. Helps communication with the operating system
4. Easy replacement for many if-else

- dictionary
Look for for Key, gives us the Value

``` python

nameofdictionary = {}
nameofdictionary[key] = value
nameofdictionary[key] = value

```
[Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.](https://docs.python.org/2/tutorial/datastructures.html#dictionaries)

### My Task for the day!
### Make a convertor using dictionary  
 ``` python

import sys
Unit = ''
Number = 0
Newline = str(os.linesep)
print str(sys.argv[0])
result = 0
if len(sys.argv) == 3:
	Unit = sys.argv[1]
	Number = float(sys.argv[2])


else:
	print "You have not typed all the parameters for this conversion program'

lookup_dictionary = {}
lookup_dictionary['m'] = 3.28
lookup_dictionary['km'] = 0.62
lookup_dictionary['L'] = 0.26
lookup_dictionary['cm'] = 0.39
factor = lookup_dictionary[Unit]
result = factor * Number
print str(result)

```

__Thank you Master Roshi!__

__Follow this GOAT for amazing softwares!!!__

[https://github.com/shinroo/](https://github.com/shinroo/)

