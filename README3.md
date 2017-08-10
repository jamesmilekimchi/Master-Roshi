# Project Master Roshi
##Day 3
Things I learnt:

- Making Variables
``` python 

Unit = ''
Number = 0

```

- (sys.agrv[])
1. Goes in order: 0,1,2 etc
2. len(sys.argv) means number of parameter


- dictionary
Look for for Key, gives us the Value

``` python

nameofdictionary = {}
lookup_dictionary[key] = value
lookup_dictionary[key] = value

```
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

