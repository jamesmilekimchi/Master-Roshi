# Project Master Roshi 
## Day 4

Things I learnt:
- __import matplotlib.pyplot as plt__

[pyplot is matplotlib's plotting framework. That specific import line merely imports the module "matplotlib.pyplot" and binds that to the name "plt".](https://www.quora.com/What-does-import-matplotlib-pyplot-as-plt-really-mean)

1. Import definiton\: Getting the codes from mac system to my Prgram

2. plt.plt\:editing the graph
Many options including Line style,Line width, line color etc

```python 

plt.plot([10,20,30,40], linestyle= 'dashed', linewidth= 3.0, 'r-')

```
3. different desgin of lines

```python

#the r is the color red, and the dash (-) means dashes
'r-' 
#the b is the color blue, and the (o) means dotted
'bo'

```

4. plt.plot also used as X and Y values

	* Or we simply call them __Domain__ and __Range__

```python

plt.plot([1,2,3,4,5,6,7,8,9,10], [1,3,5,7,9,9,7,5,3,1])

```

5. axis

[The axis() command in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies the viewport of the axes.](https://matplotlib.org/users/pyplot_tutorial.html)

``` python

plt.axis([0, 10, 0, 10])

```

	* If one gives no axis, it gives the __view of best fit__.

- How to add Image to Git

```python

Name of you graph: 
![alt text](https://whereever.you.get.the.picture.com "Name of the picture")
#the words in the " " is the words that shows when someone hovers their mouse over it

```
Dotted Line Graph: 
![alt text](https://github.com/jamesmilekimchi/Master-Roshi/blob/master/Dotted%20line%20graph.png "Dotted Line Graph")

Scattered Graph:
![alt text](https://github.com/jamesmilekimchi/Master-Roshi/blob/master/scatter%20graph.png "Scattered Graph")

## My mission of the Day!!

__MAKE A GRAPHING CALCULATOR__

```python

import matplotlib.pyplot as plt
import sys
m = 0.0
c = 0.0
print str(sys.argv[0])
result = 0

if len(sys.argv) == 3:
   m = sys.argv[1]
   c = float(sys.argv[2])


else:
   print "You have not typed the correct equation"

m = float(m)
c = float(c)
Domain = range(-100, 100)
Range = []
for x in Domain:
	Range.append(m*x + c)


plt.plot(Domain, Range, 'b-')
plt.show()

```

### One should first write the Program Name and then type the (m) which is the slope and then the y intercept. Then the Calculator will graph you the equation!!!

__Thank you Master Roshi!__

__Follow this GOAT for amazing softwares!!!__

[https://github.com/shinroo/](https://github.com/shinroo/)

