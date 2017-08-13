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

plt.plot([1,2,3,4,5,6,7,8,9,10], [1,3,5,7,9,9,7,5,3,1], 'r-')

```

