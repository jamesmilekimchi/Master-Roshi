# -*- coding: utf-8 -*-
#!/usr/bin/python

# different datatypes
#boolean_variable = True
#print type(boolean_variable)

#string_variable = "Hello"
#print type(string_variable)

#integer_variable = 10
#print type(integer_variable)

#float_variable = 10.0
#print type(float_variable)

# conditional statements
#if (boolean_variable == True):
#	print "the boolean variable is true"
#else:
#	print "the boolean variable is false"

# loops
#
#counter = 1
#while (boolean_variable == True):
#	counter += 1
#	if (counter == 17):
#		boolean_variable = False
#	else:
#		print "We haven't reached 17 yet, current value %d" % counter

#x = 'lol'
#for Roshi in range(100):
#	print x

# functions
#def add(a,b):
#	return a+b

# lists
#x = []

#x.append(1)
#x.append(2)

#for n in x:
#	print str(n)
#print str(x)

#del x[0]

#print str(x)

#x.append(1)

#print x.index(1)

#x.reverse()

#print str(x)

#print x.index(1)

#x.append(1)
#x.append(0)
#x.append(3)

#print str(x)

#x.sort()

#print str(x)

# dictionaries
# sets of key value pairs, value can be anything, even another dictionary

#y = {}
#y['robert'] = 2
#y['awiodawponopsgnsoenseoihfpsefhüs0'] = "value2"

#print str(y.keys())

#for key in y.keys():
#	print y[key]

#for key, value in y.iteritems():
#	#print "Key %s : Value %s" % (key, value)
#	print "Key " + str(key) + " : Value " + str(value)

# command line arguments
import sys

print str(sys.argv[0])

if len(sys.argv) == 2:
	print "You passed the command line argument %s" % (sys.argv[1])
else:
	print "You must pass exactly 2 arguments to python\nThe second being the variable, the first the name of the program\nYou passed %d" % (len(sys.argv))
