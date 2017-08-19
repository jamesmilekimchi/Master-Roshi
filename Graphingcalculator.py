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

